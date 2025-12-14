# -*- coding: utf-8 -*-
# @CreateTime : 2024/1/13 013 22:29
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/demo.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

import random

# text = "computer"
# print(text[0:2])  # 前闭后开
# print(text[2:-1])  # 前闭后开
# print(text[2:])  # 前闭后开 mpute
# print(text[:])  # 前闭后开 mpute

# name = "computer science"
#
# for item in name:
#     print(item, end=" ")
#
# print()
#
# count = 0
# while count < len(name):
#     print(name[count], end=" ")
#     count += 1

# # 查询某个目录所有文件 判断文件扩展名是否为 md/MD
# import os
# data_list = os.listdir(r"D:\TextFiles\MDFiles\my_note\考研")
# for item in data_list:
#     if item.split('.')[-1].upper() == 'MD':
#         print(item)

# user_list = ["计算机", "电脑", "计算器"]
# user_list.insert(1, "超级计算机")
# print(user_list)

# data_list = ['计算机', '超级计算机', '电脑', '计算器', 'computer', 'science']
#
# data_ = random.choice(data_list)  # 去列表里面随机抽取一个值
# print(data_)

# data_list = ['计算机', '超级计算机', '电脑', '计算器', 'computer', 'science']
# data_list.pop(2)
# print(data_list)

# data_list = ['计算机', '超级计算机', '电脑', '计算器', 'computer', 'science']
# delete_data = data_list.pop(2)
# print(data_list)
# print(delete_data)

# data_list = ['计算机', '超级计算机', '电脑', '计算器', 'computer', 'science']
# data_list.clear()
# print(data_list)

# data_list = [10, 2, -1, 92, 10, 25, 65]
# data_list.sort()  # 从小到大排序
# print(data_list)
#
# data_list.sort(reverse=True)  # 从小到大排序
# print(data_list)

# data_list = ['计算机', '科学', '技术']
# data_list.sort()
# print(data_list)

# v1 = 123
# res = hash(v1)
# print(res)
#
# v2 = 'computer'
# res = hash(v2)
# print(res)
#
# v3 = (11, 22, 33)
# res = hash(v3)
# print(res)

# v1 = [123, 456]
# res = hash(v1)
# print(res)

# info = {
#     'name': 'computer',
#     'age': 10,
#     'status': True,
#     'hobby': ['sing', 'dance', 'rap', 'basketball']
# }
# # 在字典中根据键获取对应的值
# v1 = info.get("name")
#
# # 若没有 返回空（None）
# v2 = info.get("email")
#
# # 如若找不到，返回指定类型
# v3 = info.get("email", "xxx")
# print(v1, v2, v3, end=' ')

# info = {
#     'name': 'computer',
#     'age': 10,
#     'status': True,
#     'hobby': ['sing', 'dance', 'rap', 'basketball']
# }
#
# # 获取所有的键
# dict_object = info.keys()  # 返回值是一个高仿的列表
# print(dict_object)
#
# print('|', end='')
# for item in info.keys():
#     print(item, end='|')

# info = {
#     'name': 'computer',
#     'age': 10,
#     'status': True,
#     'hobby': ['sing', 'dance', 'rap', 'basketball']
# }
# v1 = list(info.keys())  # 将这个高仿的列表转换成列表
# print(v1)

# info = {
#     'name': 'computer',
#     'age': 10,
#     'status': True,
#     'hobby': ['sing', 'dance', 'rap', 'basketball']
# }
# v1 = list(info.values())  # 将这个高仿的列表转换成列表
# print(v1)

# info = {
#     'name': 'computer',
#     'age': 10,
#     'status': True,
#     'hobby': ['sing', 'dance', 'rap', 'basketball']
# }
# print(info.items())
# v1 = list(info.items())  # 将这个高仿的列表转换成列表
# print(v1)

# info = {
#     'name': 'computer',
#     'age': 10,
#     'status': True,
#     'hobby': ['sing', 'dance', 'rap', 'basketball']
# }
#
# for key, value in info.items():
#     print(key, value)


# # 列表的解包
# v1, v2 = [11, 22]
# print(v1, v2)
#
# # 元组的解包
# v1, v2 = (11, 22)
# print(v1, v2)

# info = {
#     'name': 'computer',
#     'age': 10,
#     'status': True,
#     'hobby': ['sing', 'dance', 'rap', 'basketball']
# }
# data = len(info)
# print(data)  # 4
#
# data = info["name"]
# print(data)

info = {
    'name': 'computer',
    'age': 10,
    'status': True,
    'hobby': ['sing', 'dance', 'rap', 'basketball']
}

# # 修改
# info["age"] = 100
# # 新增
# info["email"] = 'xxxxxx@xx.com'
# # # 删除(若键不存在 那么删除会报错)
# # del info["age"]
#
# # 判断键是否存在
# if 'age' in info:
#     print('yes')
# else:
#     print('no')

# info = { }
# print("请输入信息，输入Q/q终止")
# while True:
#     text = input(">>> ")  # computer, 123
#     if text.upper() == 'Q':
#         break
#     else:
#         string = text.split(",")[0]
#         number = int(text.split(",")[1])
#         info[string] = number
# for key, value in info.items():
#     print(key, value)

string = """
SZ300019,硅宝科技,9.50,+0.53,+5.91%,-6.13%,423.46万，3943.10万，1.55%,24.58,1.65%,31.40亿
SZ002756，永兴材料，16.18,+0.90,+5.89%,-7.34%,247.83万，3910.01万，1.34%,18.38,2.98%,58.21亿
SZ002498，汉缆股份，6.11,+0.34,+5.89%,+102.99%,2.01亿，12.04亿，6.05%,43.98,0.62%,202.93亿
SZ002980，华盛昌，62.41,+3.46,+5.87%,+319.14%,969.65万，5.99亿，29.09%,51.97,-,83.21亿
SZ002371，北方华创，176.88,+9.80,+5.87%,+101.00%,1006.35万，17.45亿，2.20%,276.58,0.04%,875.76亿
SZ300139，晓程科技，8.71,+8.48,+5.83%,+0.23%,4423.87万，3.82亿，20.11%，亏损，0.00%,23.84亿
SZ000636，风华高科，24.51,+1.33,+5.74%,+64.61%,5605.61万，13.61亿，6.26%,71,71,8.00%,219.42亿
SZ000564，供销大集，4.06,＋日．22,+5.73%,+69.87%,2.98亿，11.89亿，14.86%，亏损，8.08%,244.52亿
SZ002612，朗姿股份，7.84,+0.42,+5.66%,-19.34%,548.71万，4191.22万，2.31%,1224.17,4.23%,34.69亿
SH600176，中国巨石，9.39,+0.50,+5.62%,-13.85%,3256.19万，3.02亿，0.93%,16.97,2.14%,328.87亿
SH603313，梦百合，24.10,+1.28,+5.61%,+14.16%,356.10万，8446.14万，1.05%,21.72,0.00%,82.23亿
SZ300279，和晶科技，5.49,+8.29,+5.58%,-8.50%,2328.20万，1.31亿，5.33%，亏损，0.00%,24.65亿
"""
new_string = string.replace("，", ",").replace(" ", "")
print(new_string)
# END
