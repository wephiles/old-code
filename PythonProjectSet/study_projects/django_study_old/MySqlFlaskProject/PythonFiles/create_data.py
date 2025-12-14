# -*- coding: utf-8 -*-
# @CreateTime : 2023/5/4 22:47
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/create_data.py
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

# 发送指令 千万不要用字符串格式化 — format 去做SQL的拼接，因为容易被SQL注入。
# 应该用pymysql内部提供的方法去做
# sql = 'insert into admin (username, password, mobile) values ("xxxx", "xxxxxxx", "18888888888")'
# cursor.execute(sql)

# # 下面是两种正确的做法
# # 下面是pymysql内部的sql语句格式
# another_sql = 'insert into admin (username, password, mobile) values (%s, %s, %s)'
# cursor.execute(another_sql, ("hhh", "123456", "16666666666"))


the_sql = 'insert into admin (username, password, mobile) values (%(n1)s, %(n2)s, %(n3)s)'
cursor.execute(the_sql, {"n1": "哈哈哈", "n2": "123456789", "n3": "11111111111"})
conn.commit()  # 这个是必须的！！！

# 关闭cursor和链接
cursor.close()
conn.close()

# END
