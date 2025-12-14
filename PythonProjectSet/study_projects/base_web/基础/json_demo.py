# -*- coding: utf-8 -*-
# @CreateTime : 2024/2/26 026 18:25
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/json_demo.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles


import decimal
import json

# import pprint
#
# info = {"k1": 123, "k2": (11, 22, 33, 44)}
# res = json.dumps(info)
# pprint.pprint(res)
# data_string = '{"k1": 123, "k2": [11, 22, 33, 44]}'
# res = json.loads(data_string)
# pprint.pprint(res)
# info = {"name": "计算机", "age": 19}
#
# res = json.dumps(info, ensure_ascii=False)
# print(res)

data = decimal.Decimal("0.3")
info = {"name": "计算机", "age": 19.5, "f": True, "hobby": None, "xx": data}
res = json.dumps(info, ensure_ascii=False)
print(res)
# --END--
