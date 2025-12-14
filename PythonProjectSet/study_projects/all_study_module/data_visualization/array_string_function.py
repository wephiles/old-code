# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/23 18:18:59
# @Project: Pycharm_Project_Set
# @File : array_string_function.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

import numpy as np


if __name__ == '__main__':
    # print(np.char.add(['hello'], [' world']))  # ['hello world']
    # print(np.char.add(['hello ', 'hi '], ['world', 'word']))  # ['hello world' 'hi word']
    # # numpy.char.multiply() 函数执行多重连接。
    # print(np.char.multiply('hello', 3))  # hellohellohello

    # np.char.center(str , width,fillchar) ：
    # str: 字符串，width: 长度，fillchar: 填充字符
    print(np.char.center('Runoob', 21, fillchar='*'))  # ********Runoob*******
    pass
