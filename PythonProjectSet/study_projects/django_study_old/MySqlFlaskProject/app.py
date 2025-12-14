# -*- coding: utf-8 -*-
# @CreateTime : 2023/5/3 20:37
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/app.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/index')
def index():
    # 找到index.html的文件，读取所有的内容
    # flask会找到index.html中的特殊占位符，将数据替换
    # 将替换完成的字符串返回给用户浏览器

    # 目前写死的
    # 但是以后可以增加和删除
    users = ['buweishi', 'shuaige', 'meinv', 'dageda', 'niuma']
    return render_template('index.html', title='示例表格', data_list=users)


if __name__ == "__main__":
    app.run()

# END
