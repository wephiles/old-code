# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/5 005 15:45
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : first_web
# @FileName : first_web/run.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)


@app.route("/add/user", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        return render_template("add_user.html")
    user_name = request.form.get("user")
    password = request.form.get("pwd")
    mobile = request.form.get("mobile")
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="637847",
        port=3306,
        db="unicom",
        charset="utf8"
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "insert into user_info (username, password, mobile) values(%s, %s, %s)"
    cursor.execute(sql, (user_name, password, mobile))
    conn.commit()

    cursor.close()
    conn.close()
    # return "添加成功：" + user_name + "|" + password + "|" + mobile
    return render_template("show_info.html",
                           user_name=user_name,
                           password=password,
                           mobile=mobile, )


@app.route("/show/user")
def show_user():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="637847",
        port=3306,
        db="unicom",
        charset="utf8"
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from user_info"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    cursor.close()
    conn.close()

    # return data_list
    return render_template("show_user.html", data_list=data_list)


if __name__ == '__main__':
    app.run()

# --END--
