# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/27 17:55:27
# @Project: Pycharm_Project_Set
# @File : decorator_01.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

from functools import wraps


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return 'Function will not run!'
        if can_run:
            return 'Function will run!'
        return f(*args, **kwargs)
    return decorated


@decorator_name
def a_func():
    return 'Function is running!'


if __name__ == '__main__':
    can_run = True
    print(a_func())

    can_run = False
    print(a_func())
    pass

# END
