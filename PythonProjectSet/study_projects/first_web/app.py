# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/3 003 23:18
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : first_web
# @FileName : first_web/app.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index")
def index():
    users = ["computer", "science", "technology", "software"]

    # 找到index.html文件,读取所有内容
    # 找到内容中特殊的占位符,并将数据进行替换
    # 将替换完成的字符串返还给用户的浏览器
    return render_template("index.html",
                           title="这个是测试占位符{{}}的",
                           data_list=users)


if __name__ == '__main__':
    app.run()

# --END--
