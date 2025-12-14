# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/20 16:46:29
# @Project: Pycharm_Project_Set
# @File : create_array_from_exists.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

import numpy as np


if __name__ == '__main__':
    """
    从存在的数组创建数组 
    """
    # numpy.asarray 类似 numpy.array   numpy.asarray(a, dtype = None, order = None)
    # 转换列表为ndarray
    # x = [[1, 2, 3], [4, 5, 6]]
    # a = np.asarray(x)
    # print(a)

    # 转换元组为array
    # x = ((1, 2, 3), (4, 5, 6), [7, 8, 9])  # 是可以转换成功的！
    # print(x)
    # a = np.asarray(x)
    # print(a)

    # 转换元组列表为ndarray
    # x = [(1, 2, 3,), (4, 5, 6,)]
    # # a = np.asarray(x)  # you must specify 'dtype=object' when creating the ndarray.
    # a = np.asarray(x, dtype='int32')
    # # 注意每个元组的最后一个数后面必须加一个逗号，并且元组要能构成一个array数组
    # print(a)

    # # 还可以试着的type参数
    # x = [1, 2, 3]
    # a = np.asarray(x, dtype=float)  # [1. 2. 3.]
    # print(a)

    # 动态数组： numpy.frombuffer 用于实现动态数组
    # numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
    # 注意：buffer 是字符串的时候，Python3 默认 str 是 Unicode 类型，所以要转成 bytestring 在原 str 前加上 b
    # s = b'Hello World!'
    # a = np.frombuffer(s, dtype='S1')  # [b'H' b'e' b'l' b'l' b'o' b' ' b'W' b'o' b'r' b'l' b'd' b'!']
    # print(a)

    # b = 'Hello world!'
    # a = np.frombuffer(b, dtype='S1')
    # # TypeError: a bytes-like object is required, not 'str' 要把Unicode类型的字符串转换成bytestring格式
    # print(a)

    # numpy.fromiter  numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组。
    # numpy.fromiter(iterable可迭代对象, dtype, count=-1)

    # 使用range函数创建列表对象
    list_ = range(5)
    it = iter(list_)

    # 使用迭代器创建 ndarray
    x = np.fromiter(it, dtype=float)  # [0. 1. 2. 3. 4.]
    print(x)
    pass
