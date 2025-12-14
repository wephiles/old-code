# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/1 22:02
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : flask_server.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# 这是一个小型服务器

import time
from flask import Flask

app = Flask(__name__)


@app.route('/bo_bo')
def index_bo_bo():
    time.sleep(2)
    return 'Hello Bo_bo'


@app.route('/jay')
def index_jay():
    time.sleep(2)
    return 'Hello Jay'


@app.route('/tom')
def index_tom():
    time.sleep(2)
    return 'Hello Tom'


if __name__ == '__main__':
    app.run(threaded=True)
