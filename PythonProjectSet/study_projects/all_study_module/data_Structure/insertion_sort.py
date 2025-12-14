# -*- coding: utf-8 -*-
# @CreateTime : 2023/7/20 020 22:52
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/insertion_sort.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles

import bubble_sort

a_list = bubble_sort.a_list


def insertion_sort(a_list: list[int]) -> [int]:
    if len(a_list) == 0:
        return []
    sentry = a_list[0]
    for i in range(1, len(a_list)):
        if a_list[i] < sentry:
            ...
    return a_list


print(insertion_sort(a_list))

# END
