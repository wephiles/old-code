# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/2/23 16:54:51
# @Project: Pycharm_Project_Set
# @File : shell sort.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun


# Shill sort is also an insertion sort.
# It is an improved version of simple insertion sort, also known as reduced incremental sort

import math


def shell_sort(list_data: list[int]) -> list:
    if len(list_data) <= 1:
        return list_data
    else:
        gap = 1
        while gap < len(list_data) / 3:
            gap = gap * 3 + 1
        while gap > 0:
            for i in range(gap, len(list_data)):
                temp = list_data[i]
                j = i - gap
                while j >= 0 and list_data[j] > temp:
                    list_data[j+gap] = list_data[j]
                    j -= gap
                list_data[j+gap] = temp
            gap = math.floor(gap / 3)
        return list_data


if __name__ == '__main__':
    test_list = [5, 4, 3, 2, 1]
    print(shell_sort(list_data=test_list))
    pass
