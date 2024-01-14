import time
from sklearn import set_config
from sklearn.utils import estimator_html_repr
import oss2
import oss2.credentials as credentials

set_config(display='diagram')

# Load dataset
#data = pd.read_csv('data.csv')

class Handler():
    def __init__(self):
        self.bucket = oss2.Bucket(oss2.AnonymousAuth(), 'http://oss-cn-hangzhou.aliyuncs.com', 'automl-yxc')

    def data_loader(self, url, features, target):
        """
        通过URL获取数据并返回feature和target
        """
        import pandas as pd
        self.bucket.get_object_to_file(url, 'data.csv')  
        data = pd.read_csv("data.csv")
        X = data.copy().drop([target],axis=1)
        X = X[features]
        Y = data[target]
        return X, Y

    def train(self, dataId, features, target):
        """
        使用tpot进行autoML。

        Parameters
        ----------
        description: string

            该模型的用途

        dataId: string

            进行模型训练使用的数据的Id

        target: string

            预测目标列名称
        """
        from sklearn.model_selection import train_test_split
        from tpot import TPOTRegressor
        import numpy as np
        from joblib import dump
        from joblib import load
        X, y = self.data_loader(dataId, features, target)
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize TPOT (for classification problem)
        tpot = TPOTRegressor(generations=1, population_size=2, verbosity=2, random_state=42)

        # Fit TPOT on the training data
        tpot.fit(X_train, y_train)

        # Evaluate the best model on the testing set
        print(tpot.score(X_test, y_test))

        timestamp = int(time.time())
        file_name = f"pipeline_{timestamp}.joblib"

        dump(tpot.fitted_pipeline_, file_name)

        self.bucket.put_object_from_file(file_name, file_name)

        loaded_pipeline = load(file_name)
        pipeline_html_repr = estimator_html_repr(loaded_pipeline)
        with open('pipeline_visualization.html', 'w') as file:
            file.write(pipeline_html_repr)
        pred = loaded_pipeline.predict(X_test)

        def mean_relative_error(y_true,y_pred,):
            relative_error = np.average(abs(y_true-y_pred) / y_true, axis=0)
            return relative_error

        test_r2 = mean_relative_error(y_test,pred)
        print(1 - test_r2)
        return {
            'pipeline_html_repr': pipeline_html_repr,
            'pipeline_id': file_name
        }
    
    def get_connection(self):
        import mysql.connector
        connection = mysql.connector.connect(
            host='121.43.60.232',
            user='optuna',
            password='lab106@ces@SHU',
            database='example'
        )
        return connection


    def deploy(self, model_name, pipeline_id):
        connection = self.get_connection()
        cursor = connection.cursor()
        create_table_query = """
            CREATE TABLE IF NOT EXISTS deployedModels (
                modelName VARCHAR(255),
                model VARCHAR(255)
            )
            """
        cursor.execute(create_table_query)
        insert_query = """
            INSERT INTO deployedModels (
                modelName,
                model
            ) VALUES (%s, %s)
            """
        cursor.execute(insert_query, (model_name, pipeline_id))
        connection.commit()
        cursor.close()
        connection.close()

    def predict(self,model_name, features):
        """
        通过modelId加载模型并返回预测结果
        """
        from joblib import load
        import pandas as pd
        connection = self.get_connection()
        cursor = connection.cursor()
        select_query = """
            SELECT * from deployedModels WHERE modelName = %s
            """
        cursor.execute(select_query, (model_name,))
        result = cursor.fetchall()
        pipeline_id = result[0][1]
        # self.bucket.get_object_to_file('pipeline_model.joblib', 'pipeline_model.joblib')
        # loaded_pipeline = load('pipeline_model.joblib')
        self.bucket.get_object_to_file(pipeline_id, pipeline_id)
        loaded_pipeline = load(pipeline_id)
        data = pd.DataFrame([features])
        pred = loaded_pipeline.predict(data)
        return str(pred[0])
    
if __name__ == "__main__":
    handler = Handler()
    train_res = handler.train('data.csv', ['热压温度（℃）', '热压压力（MPa）'], '延伸率（%）')
    pipeline_id = train_res['pipeline_id']
    handler.deploy('aaa1', pipeline_id)
    res = handler.predict('aaa1', {
            '热压温度（℃）': 100,
            '热压压力（MPa）': 200
        })
    print(res)
