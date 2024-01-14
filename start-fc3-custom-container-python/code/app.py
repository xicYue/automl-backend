import json
import logging
import sys
import traceback
from train import Handler
from flask import Flask, request

app = Flask(__name__)
handler = Handler()
logging.basicConfig(level=logging.INFO)


@app.route("/initialize", methods=["POST"])
def initialize():
    # See FC docs for all the HTTP headers: https://www.alibabacloud.com/help/doc-detail/132044.htm#common-headers
    request_id = request.headers.get("x-fc-request-id", "")
    print("FC Initialize Start RequestId: " + request_id)

    # do your things
    # Use the following code to get temporary credentials
    # access_key_id = request.headers['x-fc-access-key-id']
    # access_key_secret = request.headers['x-fc-access-key-secret']
    # access_security_token = request.headers['x-fc-security-token']

    print("FC Initialize End RequestId: " + request_id)
    return "Function is initialized, request_id: " + request_id + "\n"


@app.route("/invoke", methods=["POST"])
def invoke():
    # See FC docs for all the HTTP headers: https://www.alibabacloud.com/help/doc-detail/132044.htm#common-headers
    request_id = request.headers.get("x-fc-request-id", "")
    print("FC Invoke Start RequestId: " + request_id)

    print("hello world！")
    # Get function input, data type is bytes, convert as needed
    # event = request.get_data()
    # event_str = event.decode("utf-8")

    # Use the following code to get temporary STS credentials to access Alibaba Cloud services
    # access_key_id = request.headers['x-fc-access-key-id']
    # access_key_secret = request.headers['x-fc-access-key-secret']
    # access_security_token = request.headers['x-fc-security-token']

    print("FC Invoke End RequestId: " + request_id)
    data = request.stream.read()
    data = json.loads(data)
    print(data)
    res = handler.train(data['dataId'], data['feature'], data['target'])
    return res


@app.route("/deploy", methods=['POST'])
def deploy():
    data = request.stream.read()
    data = json.loads(data)
    res = handler.deploy(data['modelName'], data['pipeline_id'])
    return 'ok'

@app.route('/predict', methods=['POST'])
def predict():
     data = request.stream.read()
     data = json.loads(data)
     res = handler.predict(data['modelName'], data['features'])
     return res

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=9000)
