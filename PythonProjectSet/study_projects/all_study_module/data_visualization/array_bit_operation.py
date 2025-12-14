# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/23 18:09:51
# @Project: Pycharm_Project_Set
# @File : array_bit_operation.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

import numpy as np


if __name__ == '__main__':
    # a = np.arange(8).reshape(2, 4)
    # print(a)
    b = 13
    c = 17
    print(np.bitwise_and(b, c))

    print(np.bitwise_or(b, c))

    print(np.invert(b))

    print(np.binary_repr(40, width=8))  # 二进制表示


    pass
