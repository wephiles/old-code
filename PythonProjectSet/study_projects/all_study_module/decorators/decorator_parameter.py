# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/28 11:17:15
# @Project: Pycharm_Project_Set
# @File : decorator_parameter.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

from functools import wraps


def logit(file_name='out.log'):
    def log_decorator(func):

        @wraps(func)
        def warp_function(*args, **kwargs):
            log_string = warp_function.__name__ + ' was called'
            print(log_string)
            with open(file_name, 'a') as fp:
                fp.write(log_string + '\n')
            return func(*args, **kwargs)
        return warp_function
    return log_decorator


@logit()
def my_function():
    print('Function 1')
    pass


@logit(file_name='out_1.log')
def my_function_2():
    print('Function 2')
    pass


if __name__ == '__main__':
    my_function()
    my_function_2()
    pass
