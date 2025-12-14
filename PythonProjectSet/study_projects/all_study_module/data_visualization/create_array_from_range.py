# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/20 17:18:53
# @Project: Pycharm_Project_Set
# @File : create_array_from_range.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

import numpy as np


if __name__ == '__main__':
    # numpy.arange(start, stop, step, dtype)
    # x = np.arange(0, 6, 1)  # [0 1 2 3 4 5]
    # x = np.arange(0, 6, 1, dtype=float)  # [0. 1. 2. 3. 4. 5.]
    # print(x)

    # numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的
    # np.linspace(start, stop, num=50样本数量，默认50, \
    # endpoint=True True则包含stop值, retstep=False如果为True显示间距\
    # , dtype=None)
    # x = np.linspace(start=1, stop=10, num=10, retstep=True, dtype=float)
    # (array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.]), 1.0)
    # x = np.linspace(start=1, stop=10, num=10, dtype=float)
    # # [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
    #
    # print(x)

    # x = np.linspace(1, 1, 5)
    # print(x)

    # numpy.logspace 函数用于创建一个于等比数列
    # np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
    # base 参数意思是取对数的时候 log 的下标 默认是10
    # x = np.logspace(base=2, start=2, stop=32, num=4)
    # # [4.0000000e+00 4.0960000e+03 4.1943040e+06 4.2949673e+09]
    # print(x)

    #
    pass
