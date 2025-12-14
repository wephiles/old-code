# -*- coding: utf-8 -*-
# @CreateTime : 2024/5/26 026 15:37
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/demo6.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

from flask import Flask

app = Flask(__name__)


def auth(func):
    def inner(*args, **kwargs):
        # 判断用户是否登录 如果已登录，那么继续往下走  如果没有登录那么就回到登录页面
        # 这里是伪代码 后续学网络的时候会讲到
        res = func(*args, **kwargs)
        return res

    return inner

@auth
def index():
    return "首页"

@auth
def info():
    return "详情"

@auth
def order():
    return "排名"


def login():
    return "登录"


app.add_url_rule("/index/", view_func=index)
app.add_url_rule("/info/", view_func=info)
app.add_url_rule("/order/", view_func=order)
app.add_url_rule("/login/", view_func=login)

if __name__ == '__main__':
    app.run()

# --END--
