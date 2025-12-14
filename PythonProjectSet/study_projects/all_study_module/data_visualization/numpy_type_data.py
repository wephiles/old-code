# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/19 21:11:50
# @Project: Pycharm_Project_Set
# @File : numpy_type_data.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

import numpy as np


def numpy_type():
    # x = np.dtype(np.int32)
    # print(x)  # int32

    # int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
    # dt = np.dtype('i1')
    # print(dt)  # int8

    # 字节顺序标注
    # dt = np.dtype('<i4')
    # print(dt)

    # 首先创建结构化数据类型
    # dt = np.dtype([('age', np.int8)])
    # print(dt)  # [('age', 'i1')]

    # 将数据类型应用于 ndarray 对象
    # dt = np.dtype([('age', np.int8)])
    # a = np.array([(10,), (20,), (30,)], dtype=dt)  # [(10,) (20,) (30,)]
    # a = np.array([(10,), (20,), (30,)])
    # print(a)
    # 输出结果：
    # [[10]
    # [20]
    # # [30]]
    # a = np.array([(10, 11), (20, 21), (30, 31)])
    # print(a)
    """
    [[10 11]
    [20 21]
    [30 31]]
    """

    # # 类型字段名可以用于存取实际的 age 列
    # dt = np.dtype([('age', np.int8)])
    # a = np.array([(10,), (20,), (30,)], dtype=dt)
    # print(a['age'])  # [10 20 30]
    # print(a['age'][1])  # 20

    # 定义一个结构化数据类型 student 包含
    # 字符串字段 name 整数字段 age  浮点字段 marks
    # 将这个 dtype 用于 ndarray 对象
    student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
    # print(student)  # [('name', 'S20'), ('age', 'i1'), ('marks', '<f4')]
    a = np.array([('abc', 21, 50), ('xyz', 18, 75), ('hhh', 20, 90)], dtype=student)
    print(a)  # [(b'abc', 21, 50.) (b'xyz', 18, 75.) (b'hhh', 20, 90.)]
    print(a['name'])  # [b'abc' b'xyz' b'hhh']
    pass


if __name__ == '__main__':
    numpy_type()
    pass
