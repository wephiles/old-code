# -*- coding: utf-8 -*-
# @CreateTime : 2023/3/15 18:53
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/flask_severe.py
# @Description : 一个服务器
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/JinYu-2023?tab=repositories

from flask import Flask
import time

app = Flask(__name__)


@app.route('/xiaobu')
def index_xiaobu():
    time.sleep(2)
    return 'hello xiaobu'


@app.route('/jay')
def index_jay():
    time.sleep(3)
    return 'Hello jay'


@app.route('/tom')
def index_tom():
    time.sleep(3)
    return 'Hello jay'


if __name__ == '__main__':
    app.run(threaded=True)

# END
