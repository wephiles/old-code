# -*- coding: utf-8 -*-
# @CreateTime : 2024/3/5 005 21:28
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/time_model.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles


import datetime

v1 = datetime.datetime.now()    
print(v1)  # 2024-03-05 21:36:03.775433  --  datetime对象类型的数据 不是字符串！！！

# 转换datetime成字符串
str_date = v1.strftime("%Y-%m-%d %H:%M%S")
print(str_date)

# --END--
