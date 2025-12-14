# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/27 17:07:57
# @Project: Pycharm_Project_Set
# @File : decorator_principle.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

# 装饰器 就是在函数外部修改函数功能
from functools import wraps

#
# def hi(name='buweihsi'):
#     print('hi() function, ', end=' ')
#     print(name)
#
#     def greet():
#         return 'greet() function inside hi() function'
#
#     def welcome():
#         return 'welcome() function inside hi() function'
#
#     if name == 'buweishi':
#         return greet
#     else:
#         return welcome


# if __name__ == '__main__':
    # hi('emmm')
    # print(greet())  # NameError: name 'greet' is not defined
    # a = hi()  # <function hi.<locals>.welcome at 0x000002DFD9C78B80>
    # print(a)
    # b = hi('emmm')  # <function hi.<locals>.welcome at 0x000002DFD9C78C10>
    # print(b)
    # print(hi()())
    # pass


# def hi():
#     return 'hi, buweishi'
#
#
# def a_function_add_hi(func):
#     print('I am doing some boring work before executing hi()')
#     print(func())
#     print('I am okay! I had ended the hi(), it fell great!')
#     pass
#
#
# if __name__ == '__main__':
#     a_function_add_hi(hi)
#     pass


def a_new_decorator(a_func):
    @wraps(a_func)
    def wrap_function():
        print('I am doing some boring work before executing a_func()')
        a_func()
        print('I am doing some boring work after executing a_func()')

    return wrap_function


@a_new_decorator
def a_function_need_decorator():
    """Okay. this function need to be decorated! """
    print('I am the function which needs some decoration to remove my foul smell')
    # todo: Do something, but do not know what should I do!
    pass


if __name__ == '__main__':
    # a_function_need_decorator()

    # a_function_need_decorator = a_new_decorator(a_function_need_decorator)
    # # now a_function_need_decorator is wrapped by wrap_function()
    # a_function_need_decorator()

    a_function_need_decorator()
    # Attention: the statement  @a_new_decorator is just a short way of saying:
    # now a_function_need_decorator is wrapped by wrap_function()

    print(a_function_need_decorator.__name__)  # wrap_function
    # Damn, the function a_function_need_decorator() was replaced by wrap_function()

    # Fortunately, python give us a very simple function to resolve this problem:
    # functools.wraps
    # We need to import something: from functools import wraps
    # We just to to like this:
    # def a_new_decorator(a_func):
    #     @wraps(a_func)
    # Okay, everything is gone, it is perfect!

    pass
