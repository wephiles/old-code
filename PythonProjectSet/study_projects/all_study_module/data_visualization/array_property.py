# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/19 21:45:21
# @Project: Pycharm_Project_Set
# @File : array_property.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

import numpy as np
# axis=0，表示沿着第 0 轴进行操作，即对每一列进行操作；axis=1，表示沿着第1轴进行操作，即对每一行进行操作。


if __name__ == '__main__':
    # x1 = np.array([1, 2, 3])
    # print(x1)

    # ndarray.ndim 用于返回数组的维数，等于秩。
    # a = np.arange(24)
    # print(a)
    # print(a.ndim)  # a 现只有一个维度
    # 现在调整其大小
    # b = a.reshape(12, 2)  # b 现在拥有两个维度
    # b = a.reshape(8, 3)  # 现在拥有两个维度
    # b = a.reshape(6, 4)  # 现在拥有两个维度

    # b = a.reshape(2, 3, 4)  # 现在拥有三个维度
    # b = a.reshape(2, 4, 3)  # 现在拥有三个维度
    # print(b)
    # print(b.ndim)

    # ndarray.shape 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，
    # 即 ndim 属性(秩)。比如，一个二维数组，其维度表示"行数"和"列数"。
    # a = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])  # (2, 2, 3)
    # print(a.shape)
    # # shape 还能调整数组大小
    # a.shape = (2, 3, 2)
    # print(a)
    # 输出结果：
    # [[[1  2]
    #   [3  4]
    #  [5  6]]
    #
    # [[7  8]
    #  [9 10]
    # [11
    # 12]]]
    # ndarray.itemsize 以字节的形式返回数组中每一个元素的大小。
    # ndarray.flags 返回 ndarray 对象的内存信息
    pass
