FROM python:3.9-buster

WORKDIR /usr/src
RUN pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python -m pip install mysql-connector-python
COPY . .

CMD [ "python", "-u", "/usr/src/app.py" ]
