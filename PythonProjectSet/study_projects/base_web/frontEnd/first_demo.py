# -*- coding: utf-8 -*-
# @CreateTime : 2024/5/1 001 18:03
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/first_demo.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

from flask import Flask, render_template

app = Flask(__name__)


# 创建了网址 /show/info 和函数 index 的映射关系
# 以后用户在浏览器访问 http://localhost:5000/show/info 时，会自动执行 index 函数
@app.route('/show/info/')  # 注意最后面不带斜杠
def index():
    # 调用 render_template 函数，传入模板文件名和数据字典，Flask自动打开来这个文件 读取内容 返回渲染后的 HTML 代码
    # 这个文件默认回去当前项目目录下的templates文件夹中找
    return render_template('index.html', name='wephiles')


@app.route('/goods/list/')  # 注意最后面不带斜杠
def goods_list():
    # 调用 render_template 函数，传入模板文件名和数据字典，Flask自动打开来这个文件 读取内容 返回渲染后的 HTML 代码
    # 这个文件默认回去当前项目目录下的templates文件夹中找
    return render_template('goods_list.html', name='wephiles')


@app.route("/get/news/")
def get_news():
    return "<h1>get news</h1>"


@app.route("/user/list/")
def user_list():
    return render_template("user_list.html", name="JinYu")


@app.route("/user/register/")
def register():
    return render_template("register.html", name="JinYu")


if __name__ == '__main__':
    app.run()

    # 自定义主机和端口号
    # app.run(host="", port="")

# --END--
