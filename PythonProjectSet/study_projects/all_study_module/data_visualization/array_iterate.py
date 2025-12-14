# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/20 22:12:55
# @Project: Pycharm_Project_Set
# @File : array_iterate.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

import numpy as np


def main():
    """
    NumPy 迭代数组
    NumPy 迭代器对象 numpy.nditer 提供了一种灵活访问一个或者多个数组元素的方式
    """
    # a = np.arange(6).reshape(2, 3)
    # print(a)
    # print('迭代输出:')
    # for x in np.nditer(a):
    #     print(x, end=', ')  # 0, 1, 2, 3, 4, 5,
    # 以上实例不是使用标准 C 或者 Fortran 顺序，
    # 选择的顺序是和数组内存布局一致的，这样做是为了提升访问的效率，
    # 默认是行序优先（row-major order，或者说是 C-order）

    # 可以用数组转置的copy方法对比一下：
    a = np.arange(6).reshape(2, 3)
    # for x in np.nditer(a.T):
    #     print(x, end=' ')
    # print()
    # for y in np.nditer(a):
    #     print(y, end=' ')
    # print()
    # 从上述例子可以看出，a 和 a.T 的遍历顺序是一样的，
    # 也就是他们在内存中的存储顺序也是一样的，
    # 但是 a.T.copy(order = 'C') 的遍历结果是不同的，
    # 那是因为它和前两种的存储方式是不一样的，默认是按行访问。
    # print(a)
    # print(a.T)
    # print(a.T.copy(order='C'))

    # 控制遍历顺序：for x in np.nditer(a, order='F'):Fortran order，即是列序优先；
    # for x in np.nditer(a.T, order='C'):C order，即是行序优先；

    # a = np.arange(0, 60, 5)
    # a = a.reshape(3, 4)
    # print('原始数组是：')
    # print(a)
    # print('\n')
    # print('原始数组的转置是：')
    # b = a.T
    # print(b)
    # print('\n')
    # print('以 C 风格顺序排序：')
    # c = b.copy(order='C')
    # print(c)
    # for x in np.nditer(c):
    #     print(x, end=", ")
    # print('\n')
    # print('以 F 风格顺序排序：')
    # c = b.copy(order='F')
    # print(c)
    # for x in np.nditer(c):
    #     print(x, end=", ")

    # 可以通过显式设置，来强制 nditer 对象使用某种顺序：
    # a = np.arange(0, 60, 5)
    # a = a.reshape(3, 4)
    # print('原始数组是：')
    # print(a)
    # print('\n')
    # print('以 C 风格顺序排序：')
    # for x in np.nditer(a, order='C'):
    #     print(x, end=", ")
    # print('\n')
    # print('以 F 风格顺序排序：')
    # for x in np.nditer(a, order='F'):
    #     print(x, end=", ")

    # 修改数组元素的值：
    # nditer 对象有另一个可选参数 op_flags。 默认情况下，nditer 将视待迭代遍历的数组为只读对象（read-only），
    # 为了在遍历数组的同时，实现对数组元素值得修改，必须指定 read-write 或者 write-only 的模式
    # a = np.arange(0, 60, 5)
    # a = a.reshape(3, 4)
    # print(a)
    #
    # for x in np.nditer(a, op_flags=['readwrite']):
    #     x[...] = 2 * x
    # print(a)

    # 在下面的实例中，迭代器遍历对应于每列，并组合为一维数组
    # a = np.arange(0, 60, 5)
    # a = a.reshape(3, 4)
    # print('原始数组是：')
    # print(a)
    # print('\n')
    # print('修改后的数组是：')
    # for x in np.nditer(a, flags=['external_loop'], order='F'):
    #     # [ 0 20 40], [ 5 25 45], [10 30 50], [15 35 55],
    #     print(x, end=", ")

    # 广播迭代：
    # a = np.arange(0, 60, 5)
    # a = a.reshape(3, 4)
    # print('第一个数组为：')
    # print(a)
    # print('\n')
    # print('第二个数组为：')
    # b = np.array([1, 2, 3, 4], dtype=int)
    # print(b)
    # print('\n')
    # print('修改后的数组为：')
    # for x, y in np.nditer([a, b]):
    #     print("%d:%d" % (x, y), end=", ")
    #     # 0:1, 5:2, 10:3, 15:4, 20:1, 25:2, 30:3, 35:4, 40:1, 45:2, 50:3, 55:4,

    pass


if __name__ == '__main__':
    main()
    pass
