#!/user/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2024/12/17 21:19
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/约束.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# class BaseMessage(object):
#     def send():
#         # 如果有下面这行语句，只要继承这个基类就必须要重写这个send方法用于完成具体的业务逻辑 否则会报错
#         raise NotImplementedError('.send() method must be overridden!')
#
#
# class Email(BaseMessage):
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
# class Wechat(BaseMessage):
#     def send(self):
#         pass
#
#     def f3(self):
#         pass
#
#
# class Msg(BaseMessage):
#     def send(self):
#         pass
#
#     def f4(self):
#         pass
#
#
# def func(arg):
#     """
#     报警通知的功能...
#     """
#     arg.send()
#
#
# obj = Msg()
# obj.send()

# class Base(object):
#     def send(self, x):
#         raise NotImplementedError('.send() method must be implemented!')
#
#
# class Foo(Base):
#     def ok(self):
#         pass
#
#
# obj = Foo()
# obj.ok()

# from abc import ABCMeta, abstractmethod
#
#
# class Base(metaclass=ABCMeta):
#     """抽象类"""
#
#     def f1(self):
#         # 普通实例方法
#         pass
#
#     @abstractmethod
#     def f2(self):
#         # 抽象方法
#         pass
#
#
# class Foo(Base):
#     def f2(self):
#         pass
#
#
# obj = Foo()
# obj.f1()
# obj.f2()

# --END--
