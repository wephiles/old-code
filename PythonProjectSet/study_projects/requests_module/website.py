# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/16 016 10:38
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/website.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.


from flask import Flask
import time

app = Flask(__name__)


@app.route('/bobo')
def index_bobo():
    time.sleep(2)
    return 'hello bobo'


@app.route('/jay')
def index_jay():
    time.sleep(2)
    return 'hello jay'


@app.route('/tom')
def index_tom():
    time.sleep(2)
    return 'hello tom'


if __name__ == '__main__':
    app.run(threaded=True)

# --END--
