# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/19 22:04:58
# @Project: Pycharm_Project_Set
# @File : create_array.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

import numpy as np


if __name__ == '__main__':
    # numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：
    # 注意：是数组形状，不是数组！！！
    # a = np.empty([3, 3], dtype=int)
    # print(a)

    # numpy.zeros
    # 创建指定大小的数组，数组元素以 0 来填充：

    # 默认为浮点数
    # x = np.zeros(5)
    # print(x)
    #
    # # 设置类型为整数
    # y = np.zeros((5,), dtype=np.int32)
    # print(y)
    #
    # # 自定义类型
    # z = np.zeros((3, 2), dtype=[('x', 'i4'), ('y', 'i4')])
    # print(z)

    # numpy.ones
    # 创建指定形状的数组，数组元素以 1 来填充：

    # # 默认为浮点数
    # x = np.ones(5)
    # print(x)
    #
    # # 自定义类型
    # x = np.ones([2, 3], dtype=int)
    # print(x)

    pass
