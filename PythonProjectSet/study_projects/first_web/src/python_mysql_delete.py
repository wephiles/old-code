# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/5 005 15:33
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : first_web
# @FileName : first_web/python_mysql_delete.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import pymysql
from pprint import pprint

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='637847',
    database='unicom',
    charset='utf8',
)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 查询
sql = "delete from user_info where username=%s"
cursor.execute(sql, ['def', ])
conn.commit()

# data_list = cursor.fetchall()
#
# for row_dict in data_list:
#     print(row_dict)

cursor.close()
conn.close()

# --END--
