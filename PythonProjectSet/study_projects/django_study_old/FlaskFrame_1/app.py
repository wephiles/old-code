# -*- coding: utf-8 -*-
# @CreateTime : 2023/4/21 19:47
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : WebProject/app.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles


from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/register')
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        user = request.form.get('user')
        password = request.form.get('pwd')
        hobbies = request.form.getlist('hobby')
        gender = request.form.get('gender')
        city = request.form.get('selection_city')
        skill = request.form.getlist('selection_good_at')
        more = request.form.get('more')
        print(user)
        print(password)
        print(hobbies)
        print(gender)
        print(city)
        print(skill)
        print(more)

        # 将用户信息写入到文件/数据库/Excel
        return '<h1>提交以后</h1>'


@app.route('/do/reg', methods=['GET', 'POST'])
def do_reg():
    # return render_template('register.html')

    # 接收通过get发回的数据
    # 给用户返回结果
    print(request.args)
    return '<h1>提交以后</h1>'


@app.route('/post/reg', methods=['POST'])
def post_reg():

    # 接收通过post发回的数据
    # 给用户返回结果
    user = request.form.get('user')
    password = request.form.get('pwd')
    hobbies = request.form.getlist('hobby')
    gender = request.form.get('gender')
    city = request.form.get('selection_city')
    skill = request.form.getlist('selection_good_at')
    more = request.form.get('more')
    print(user)
    print(password)
    print(hobbies)
    print(gender)
    print(city)
    print(skill)
    print(more)

    # 将用户信息写入到文件/数据库/Excel
    return '<h1>提交以后</h1>'
    # return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()

# END
