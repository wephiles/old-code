# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/20 18:49:42
# @Project: Pycharm_Project_Set
# @File : array_broadcast.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

import numpy as np


def main():
    """
    本文件学习广播
    广播(Broadcast)是 numpy 对不同形状(shape)的数组进行数值计算的方式
    """
    # a = np.array([1, 2, 3, 4])
    # b = np.array([10, 20, 30, 40])
    # print(a*b)
    # 当运算中的 2 个数组的形状不同时，numpy 将自动触发广播机制。
    # a = np.array([[0, 0, 0],
    #               [10, 10, 10],
    #               [30, 30, 30],
    #               [20, 20, 20]])
    # b = np.array([[1, 2, 3], [4, 5, 6]])
    # print(a+b)
    # 4x3 的二维数组与长为 3 的一维数组相加，等效于把数组 b 在二维上重复 4 次再运算
    # b_ = np.tile(b, (4, 2))
    # tile()函数就是把第一个参数（一个数组）把数组所有行复制第二个参数的第一个值次，把列复制第二个参数的值次
    # print(b_)
    # print(a+b_)
    # print(a + b)
    # a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # b = np.array([[1, 2, 4]])
    # # 注意： 如果输入数组的某个维度和输出数组的对应维度的长度相同或者其长度为 1 时
    # print(a+b)
    pass


if __name__ == '__main__':
    main()
