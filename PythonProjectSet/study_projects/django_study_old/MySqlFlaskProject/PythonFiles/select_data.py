# -*- coding: utf-8 -*-
# @CreateTime : 2023/5/5 16:06
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/select_data.py
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

sql = 'select * from admin where id > %s'
cursor.execute(sql, (6, ))

# data_list = cursor.fetchone()
# # for item in data_list:
# #     print(item)

data = cursor.fetchone()
print(data)

cursor.close()
conn.close()

# END
