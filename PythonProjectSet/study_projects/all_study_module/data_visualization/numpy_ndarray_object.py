# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/19 20:43:15
# @Project: Pycharm_Project_Set
# @File : numpy_ndarray_object.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

import numpy as np


if __name__ == '__main__':
    # print(np.eye(4, 4))
    # numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
    # object数组或嵌套的数列,
    # dtype 数组元素的数据类型，可选,
    # copy 对象是否需要复制，可选,
    # order 创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）,
    # subok 默认返回一个与基类类型一致的数组,
    # ndmin 指定生成数组的最小维度)
    a = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], dtype=str)
    print(a)
    pass
