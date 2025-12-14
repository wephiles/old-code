# -*- coding: utf-8 -*-
# @CreateTime : 2023/3/23 20:57
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/web_01.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/JinYu-2023?tab=repositories

from flask import Flask, render_template

app = Flask(__name__)


# 创建函数和网址的对应关系
# 到时候访问网址/show/info 的时候就会自动执行main这个函数
@app.route('/show/info')
def main() -> any:
    # return r'<h1>这是一个测试的网页</h1>中国联通'
    # flask会自动打开这个文件 读取内容并给用户返回
    # 默认：去当前文件目录的templates目录下去寻找
    return render_template(r'index.html')  # 参数是：文件路径


@app.route('/get/news')
def login() -> any:
    # return r'<h1>这是一个测试的网页</h1>中国联通'
    # flask会自动打开这个文件 读取内容并给用户返回
    # 默认：去当前文件目录的templates目录下去寻找
    # return render_template(r'inde.html')  # 参数是：文件路径
    return render_template(r'login.html')  # 参数是：文件路径


@app.route('/pic/list')
def picture() -> any:
    return render_template(r'pictures.html')  # 参数是：文件路径


@app.route('/user/list')
def user_list() -> any:
    return render_template(r'user_list.html')  # 参数是：文件路径


@app.route('/register')
def register() -> any:
    return render_template(r'register.html')  # 参数是：文件路径


if __name__ == '__main__':
    app.run(host='', port=5000)  # 运行
    pass

# END
