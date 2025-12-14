# -*- coding: utf-8 -*-
# @CreateTime : 2023/5/5 17:11
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/app.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles


from flask import Flask, render_template, request
import pymysql


app = Flask(__name__)


@app.route('/add/user', methods=['POST', 'GET'])
def add_user():
    if request.method == 'GET':
        return render_template('add_user.html')
    username = request.form.get('user')
    password = request.form.get('pwd')
    phone_number = request.form.get('mobile')

    # 链接数据库
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='WarmDou_TS20866',
        charset='utf8',
        db='unicome'
    )

    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 执行sql
    try:
        sql = "insert into admin (username, password, mobile) values (%s, %s, %s)"
        cursor.execute(sql, (username, password, phone_number))
        conn.commit()
    except Exception as e:
        print(e)
    # 关闭链接
    cursor.close()
    conn.close()
    return '添加成功'


@app.route('/show/user')
def show_user():
    # if request.method == 'GET':
    #     return render_template('add_user.html')
    username = request.form.get('user')
    password = request.form.get('pwd')
    phone_number = request.form.get('mobile')

    # 链接数据库
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='WarmDou_TS20866',
        charset='utf8',
        db='unicome'
    )
    data_list = []
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 执行sql
    try:
        sql = "select * from admin"
        cursor.execute(sql)
        data_list = cursor.fetchall()
    except Exception as e:
        print(e)
    # 关闭链接

    cursor.close()
    conn.close()
    for item in data_list:
        print(item)
    return render_template('show_users.html', data_list=data_list)


if __name__ == '__main__':
    print("run")
    app.run()

# END
