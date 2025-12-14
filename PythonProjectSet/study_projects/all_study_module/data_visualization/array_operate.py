# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/20 22:37:15
# @Project: Pycharm_Project_Set
# @File : array_operate.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

import numpy as np


def main():
    """
    操作数组
    reshape	不改变数据的条件下修改形状
    flat	数组元素迭代器
    flatten	返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
    ravel	返回展开数组
    """
    # a = np.arange(9).reshape(3, 3)
    # print('原始数组：')
    # for rows in a:
    #     print(rows)
    #
    # # 对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
    # for i in a.flat:
    #     print(i, end=' ')  # 0 1 2 3 4 5 6 7 8
    # a = np.arange(8).reshape(2, 2, 2)
    # print(a)
    # print(a.flatten())  # 默认按行展开
    # print(a.flatten(order='F'))  # 按列展开

    # numpy.ravel() 展平的数组元素，顺序通常是"C风格"，返回的是数组视图（view，有点类似 C/C++引用reference的意味），修改会影响原始数组。
    # 该函数接收两个参数
    # print(a.ravel())
    # print(a.ravel(order='F'))

    # 翻转数组
    # numpy.transpose(arr, axes) 	对换数组的维度
    # print(a.transpose())
    # print(np.transpose(a))  # 此语句和上条语句等价
    # print(a.T)   # 转置，类似于transpose
    # numpy.rollaxis 函数向后滚动特定的轴到一个特定位置，numpy.rollaxis(arr, axis, start)
    # print(np.where(a == 6))
    # print(a[1, 1, 0])
    # # 将轴 2 滚动到轴 0（宽度到深度）
    # print(np.rellaxis(a, 2, 0))
    # print(np.where(a == 6))

    # numpy.swapaxes 函数用于交换数组的两个轴
    # a = np.arange(8).reshape(2, 2, 2)
    #
    # print('原数组：')
    # print(a)
    # print('\n')
    # # 现在交换轴 0（深度方向）到轴 2（宽度方向）
    #
    # print('调用 swapaxes 函数后的数组：')
    # print(np.swapaxes(a, 2, 0))
    # a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # print(a)
    # print('滚动后:')
    # print(np.rollaxis(a, 0, 0))
    # a = np.arange(12).reshape(2, 2, 3)
    # print(a)
    # numpy.broadcast 用于模仿广播的对象，它返回一个对象，该对象封装了将一个数组广播到另一个数组的结果。
    # 该函数使用两个数组作为输入参数
    # x = np.array([[1], [2], [3]])
    # y = np.array([4, 5, 6])
    #
    # # 对 y 广播 x
    # b = np.broadcast(x, y)  # b 此时拥有 iterator属性 基于自身组件的迭代器元组
    # r, c = b.iters
    # print(next(r), next(c))
    # print(next(r), next(c))
    #
    # print(b.shape)
    # b = np.broadcast(x, y)
    # c = np.empty(b.shape)
    #
    # c.flat = [u + v for (u, v) in b]
    # print(c)

    # numpy.broadcast_to 函数将数组广播到新形状。它在原始数组上返回只读视图。
    # 它通常不连续。 如果新形状不符合 NumPy 的广播规则，该函数可能会抛出ValueError
    a = np.array([1, 2, 3, 4]).reshape(1, 4)
    print(a)
    print('\n')

    print(np.broadcast_to(a, (4, 4)))
    pass


if __name__ == '__main__':
    main()
    pass
