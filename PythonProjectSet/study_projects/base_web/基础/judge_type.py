# -*- coding: utf-8 -*-
# @CreateTime : 2024/2/25 025 20:39
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/judge_type.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles


import pprint as pp

# age = 12
#
#
# def func():
#     return 123
#
#
# v1 = callable(age)
# v2 = callable(func)
#
# print(v1, v2)

# goods = ["computer", "huawei", "xiaomi", "oppo"]
# # 以前
# for i in range(len(goods)):
#     msg = "{} {}".format(i + 1, goods[i])
#     print(msg)

# goods = ["computer", "huawei", "xiaomi", "oppo"]
# # 以前
# for i in range(len(goods)):
#     msg = "{} {}".format(i + 1, goods[i])
#     print(msg)
#
# # 现在
# goods = ["computer", "huawei", "xiaomi", "oppo"]
# for index, item in enumerate(goods, 1):  # 那个1表示起始值
#     msg = "{} {}".format(index, item)

# data_list = ["1", "2", "3", "10", "12"]
# new_data = sorted(data_list)
# print(new_data)

# data_list = ["1 哈哈好", "2 嗯嗯", "3 哈哈哈", "10 嗯嗯呢", "12 哈哈好"]
#
#
# # 自定义排序规则 函数返回什么 那就按照返回的值进行排序
# def func(arg):
#     return int(arg.split(" ")[0])
#
#
# new_data = sorted(data_list, key=func)
# print(new_data)

# data_list = ["1 哈哈好", "2 嗯嗯", "3 哈哈哈", "10 嗯嗯呢", "12 哈哈好"]
# func = lambda arg: int(arg.split(" ")[0])
# new_data = sorted(data_list, key=func)
# print(new_data)

# data_list = ["工号-{}".format(i) for i in range(4)]
# print(data_list)

# data_list = [1, True, "com", "sci", [11, 22], 99, 123, (45,)]
# result = [i for i in data_list if isinstance(i, int)]

# data = {i: (i, 100) for i in range(10)}
# pp.pprint(data)

# text = (r"https://www.sogou.com/web?query=xx&_asf=www.sogou.com&_ast=&w=01019900&p=40040100&ie=utf8&"
#         r"from=index-nologin&s_from=index&sut=19&sst0=1708868657212&lkt=0%2C0%2C0&"
#         r"sugsuv=1708868652598249&sugtime=1708868657212")
# # 将字符串转换为字典： {"query": xx, "_asf": xxxx, ...}
#
# data_dict = {i.split("=")[0]: i.split("=")[1] for i in text.split("?")[1].split("&")}
# pp.pprint(data_dict)

# a_dict = {
#     '_asf': 'www.sogou.com',
#     '_ast': '',
#     'from': 'index-nologin',
#     'ie': 'utf8',
#     'lkt': '0%2C0%2C0',
#     'p': '40040100',
#     'query': 'xx',
#     's_from': 'index',
#     'sst0': '1708868657212',
#     'sugsuv': '1708868652598249',
#     'sugtime': '1708868657212',
#     'sut': '19',
#     'w': '01019900'
# }
# data_list = ["{}={}".format(k, v) for k, v in a_dict.items()]
# pp.pprint(data_list)
# print("&".join(data_list))

# --END--
