# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/17 017 11:21
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/iter_tools.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles


import itertools

data_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
             [11, 22, 33, 44],
             [111, 222, 333, 444]]


data = list(itertools.chain(*data_list))

print(data)

# --END--
