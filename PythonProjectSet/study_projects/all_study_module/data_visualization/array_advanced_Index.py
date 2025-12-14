# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/20 17:50:21
# @Project: Pycharm_Project_Set
# @File : array_advanced_Index.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

import numpy as np


def main():
    """
    learn advanced index
    """
    # 数组可以由整数数组索引、布尔索引及花式索引

    # 整数数组索引：
    # 以下实例获取数组中
    # (0,0)
    # (1,1)
    # (2,0)位置处的元素。
    # x = np.array([[1, 2], [3, 4], [5, 6]])
    # y = x[[0, 1, 2], [0, 1, 0]]
    # print(y)

    # 以下实例获取了 4X3 数组中的四个角的元素。 行索引是 [0,0] 和 [3,3]，而列索引是 [0,2] 和 [0,2]
    # x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
    # print(x)
    # y = x[[0, 3, 0, 3], [0, 0, 2, 2]]  # [ 0  9  2 11]
    # print(y)

    # 这两行代码看竖列就可以啦
    # y = np.array([[0, 0], [3, 3]])  # 行索引
    # z = np.array([[0, 2], [0, 2]])  # 列索引
    # 意思就是，行是从0 0 3 3里面按顺选，列从0 2 0 2 里面按顺序选，选出来后按顺序找出元素

    # t = x[y]
    # print('t:', end=' ')
    # print(t)
    # h = x[y, z]
    # print(h)

    # 可以借助切片 : 或 … 与索引数组组合
    # a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # b = a[1:3, 1:3]
    # c = a[1:3, [1, 2]]
    # d = a[..., 1:]
    # print(b)
    # print(c)
    # print(d)

    # 布尔索引
    # x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
    # print('大于 5 的元素是：')
    # print(x[x > 5])

    # 用~（取补集符号）
    # x = np.nan
    # a = np.array([x, 1, 2, x, 3, 4, 5])
    # 过滤nan:
    # print(a[~np.isnan(a)])  # [1. 2. 3. 4. 5.]

    # 过滤非复数元素
    # a = np.array([1, 2+6j, 5, 3.5+1j])
    # print(a[np.iscomplex(a)])

    # # 花式索引 花式索引跟切片不一样，它总是将数据复制到新数组中
    # 传入顺序索引数组
    # x = np.arange(32).reshape((8, 4))
    # print(x)
    # print('\n')
    # print(x[[4, 2, 1, 7]])
    # print()

    # # 传入倒序索引数组
    # print(x[[-4, -2, -1, -7]])

    # 传入多个索引数组（要使用np.ix_）
    x = np.arange(32).reshape((8, 4))
    print(x)
    print(x[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])
    pass


if __name__ == '__main__':
    main()
    pass
