# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/28 11:05:02
# @Project: Pycharm_Project_Set
# @File : decorator_logging.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

from functools import wraps


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + ' was called!')
        return func(*args, **kwargs)
    return with_logging


@logit
def addition(x):
    """Do something math."""
    return 2 * x


if __name__ == '__main__':
    result = addition(4)
    print(result)
    pass
