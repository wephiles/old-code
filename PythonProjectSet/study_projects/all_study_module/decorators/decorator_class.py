# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/28 11:30:13
# @Project: Pycharm_Project_Set
# @File : decorator_class.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

from functools import wraps


class Logit(object):
    """This is a decorator class."""

    def __init__(self, file_name='out_1.log'):
        self.log_file = file_name

    def __call__(self, func):
        @wraps(func)
        def wrap_function(*args, **kwargs):
            log_string = func.__name__ + ' was called.'
            with open(self.log_file, 'a') as fp:
                # 现在将日志打到指定的文件
                fp.write(log_string + '\n')

            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)
        return wrap_function

    def notify(self):
        # logit do nothing but print the log information
        pass


# @Logit()
# def my_func():
#     """Do something"""
#     pass

# Create a subclass
class EmailLogit(Logit):
    """This is an subclass which can send message to administrator."""
    def __init__(self, email='2086689759@qq.com', *args, **kwargs):
        super().__init__()
        self.email = email

    def notify(self):
        """Send a email to self.email.

        Actually, this function doing nothing but send a email.
        """
        pass


if __name__ == '__main__':
    # my_func()
    pass
