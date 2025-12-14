# -*- coding: utf-8 -*-
# @CreateTime : 2024/3/23 023 21:39
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/timedelta_demo.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

from datetime import datetime, timedelta

v1 = datetime.now()
print(v1)
res = v1 + timedelta(seconds=100)
res = v1 + timedelta(days=280)
res = v1 + timedelta(days=10, minutes=10, seconds=100)

res.strftime("%Y-%m-%d %H:%M:%S")
print(res)

# --END--
