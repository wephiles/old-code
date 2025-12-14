# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/4 004 16:31
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : first_web
# @FileName : first_web/python_mysql_add.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import pymysql

# 链接mysql
conn = pymysql.connect(host='localhost',
                       user='root',
                       port=3306,
                       password='637847',
                       charset='utf8',
                       db='unicom')

# 游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
while True:
    user_name = input("your name. >>>")
    password = input("your password. >>>")
    mobile = input("your phone number. >>>")
    if user_name.upper() == "Q" or password.upper() == 'Q' or mobile.upper() == 'Q':
        break

    sql = "insert into user_info (username, password, mobile) values(%s, %s, %s);"
    # sql1 = "insert into user_info (username, password, mobile) values(%(n1)s, %(n2)s, %(n3)s);"
    # 发送指令 千万不要用字符串格式化去做sql的拼接 安全隐患 -- SQL注入
    cursor.execute(sql, [user_name, password, mobile])
    # cursor.execute(sql1, {"n1": "computer", "n2": "987654321", "n3": "15333331111"})
    # 使用了insert必须要commit
    conn.commit()

# 关闭链接
cursor.close()
conn.close()

# --END--
