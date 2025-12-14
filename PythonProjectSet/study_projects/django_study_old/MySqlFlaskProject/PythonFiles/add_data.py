# -*- coding: utf-8 -*-
# @CreateTime : 2023/5/4 23:12
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/add_data.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles

import pymysql

# 链接mysql
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='WarmDou_TS20866',
    charset='utf8',
    db='unicome'
)
# 收发指令
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

print('如果想退出，请输入q')
while True:
    user = input('请输入用户名')
    pwd = input('请输入密码')
    mobile = input('请输入手机号')

    if user.upper() == 'Q' or pwd.upper() == 'Q' or mobile.upper() == 'Q':
        break

    sql = 'insert into admin (username, password, mobile) values (%s, %s, %s)'
    cursor.execute(sql, (user, pwd, mobile))

    conn.commit()  # 这个是必须的！！！

    # 关闭cursor和链接
    cursor.close()
    conn.close()

# END
