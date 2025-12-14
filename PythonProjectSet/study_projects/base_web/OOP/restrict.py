# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/28 028 16:22
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/restrict.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# def func(arg):
#     """
#     报警通知功能
#     Args:
#         arg ():
#
#     Returns:
#
#     """
#     arg.send()
#
#
# class BaseMessage(object):
#     """
#     潜规则，以后根据这个基类写的代码都必须要重新send方法，否则会抛出异常
#     """
#
#     def send(self, x1):
#         """
#         必须要继承BaseMessage的send方法，来完成相关的业务逻辑。
#         Returns:
#
#         """
#         raise NotImplementedError(".send()方法必须被重写！")
#
#
# class Wechat(BaseMessage):
#     def send(self):
#         pass
#
#     def f1(self):
#         pass
#
#     def f2(self):
#         pass
#
#
# class Msg(BaseMessage):
#     def send(self):
#         pass
#
#     def f1(self):
#         pass
#
#     def f2(self):
#         pass
#
#
# class Email(BaseMessage):
#     pass
#
#     def send(self, x1):
#         pass
#
#
# obj = Email()
# obj.send(123)

from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):  # 定义了抽象类
    """
    抽象类，语法就是这样，记住就行了。
    """

    def f1(self):
        """
        普通方法
        Returns:

        """
        pass

    @abstractmethod
    def f2(self):
        """
        抽象方法
        Returns:

        """
        pass


class Foo(Base):
    pass


obj = Foo()
obj.f1()
obj.f2()

# --END--
