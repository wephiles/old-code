# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/20 17:36:55
# @Project: Pycharm_Project_Set
# @File : array_slice_index.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

import numpy as np


if __name__ == '__main__':
    """
    切片和索引
    # """
    # a = np.arange(10)
    # s = slice(2, 7, 2)  # [2 4 6]
    # print(a[s])

    # a = np.arange(10)
    # b = a[2: 7: 2]  # [2 4 6]
    # print(b)

    # a = np.arange(10)
    # print(a[2:])
    # print(a[2:7])
    # print(a[-1:])  # [9]
    # print(a[:-1])  # [0 1 2 3 4 5 6 7 8]

    # 对矩阵进行切片：
    # a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # print(a[1])  # [4 5 6]
    # print(a[1][1])  # 5

    # 切片还可以包括省略号 …，来使选择元组的长度与数组的维度相同。
    # 如果在行位置使用省略号，它将返回包含行中元素的 ndarray。
    # a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # print(a[..., 1])  # [2 5 8] 第一列
    # print(a[1, ...])  # [4 5 6] 第一行
    # print(a[..., 1:])  # 自己想，应该能想到结果是啥，注意这个 一  指的是偏移而不是实际的第几个
    pass
