# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/10 17:07
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : main_test.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# import a_function

# from a_class import People
# from a_function import copy
# print("hello")
# copy()
# x = People()
# print(x.sum_a_b_c())
def say_hi(string, width):
    """ 这是一个注释 """
    """ 下面只是个小测试 """
    # todo: print() 是一个函数，不是一个关键字，这是在 python3 出现的状况！
    # TODO: 这是个简单的测试程序
    print(string * width)
    for i in range(10, -1, -1):
        print(i)


if __name__ == '__main__':
    say_hi('hello ', 5)
    say_hi('what', 2)
    pass
