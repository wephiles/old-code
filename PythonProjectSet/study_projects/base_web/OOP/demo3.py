# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/26 026 22:22
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/demo3.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

# class Base(object):
#     pass
#
#
# class Foo(Base):
#     pass
#
#
# class Bar(Foo):
#     pass
#
#
# # 检查第一个参数是否是第二个参数的子类
# print(issubclass(Foo, Base))  # True
# print(issubclass(Base, Foo))  # False
# print(issubclass(Bar, Base))  # True

# class Foo(object):
#     pass
#
#
# class Bar(object):
#     pass
#
#
# obj = Foo()
# print(obj, type(obj))  # 获取当前对象是由哪个类创建。
#
# v = type(obj) is Foo
# print(v)
#
#
# obj1 = Foo()
# obj2 = Foo()
# obj3 = Bar()
#
#
# def func(*args):
#     foo_count = 0
#     bar_count = 0
#     for item in args:
#         if type(item) is Foo:
#             foo_count += 1
#         if type(item) is Bar:
#             bar_count += 1
#     return foo_count, bar_count
#
#
# print(func(obj1, obj2, obj3))


# class Base(object):
#     pass
#
#
# class Foo(Base):
#     pass
#
#
# class Bar(object):
#     pass
#
#
# obj = Foo()
# print(obj, isinstance(obj, Foo))  # True 检查第一个参数是否是第二个参数的实例 第一个参数一般是对象 第二个参数一般是类
# print(obj, isinstance(obj, Bar))  # False
# print(obj, isinstance(obj, Base))  # True

# def func():
#     pass
#
#
# class Foo(object):
#     def func(self):
#         pass
#
#     @staticmethod
#     def xxx():
#         pass
#
#
# print(func)  # 函数 <function func at 0x0000019B8BA5E0C0>
# print(Foo().func)  # 方法 <bound method Foo.func of <__main__.Foo object at 0x0000019B8BC016D0>>
# print(Foo().xxx)  # 函数 <function Foo.xxx at 0x00000294E219E700>
# print(Foo.xxx)  # 函数 <function Foo.xxx at 0x00000294E219E700>

from types import FunctionType, MethodType


# def func():
#     pass
#
#
# class Foo(object):
#     def func(self):
#         pass
#
#     @staticmethod
#     def xxx():
#         pass
#
#
# def check(arg):
#     """
#     检查参数是函数或者是方法
#     Args:
#         arg (object): 传递的参数
#
#     Returns:
#
#     """
#     if isinstance(arg, FunctionType):
#         print(arg.__name__, '函数')
#     if isinstance(arg, MethodType):
#         print(arg.__name__, arg.__func__.__name__, '方法')
#
#
# check(func)  # func 函数
# check(Foo().func)  # func 方法
# check(Foo.func)  # func 函数
#
# check(Foo().xxx)  # xxx 函数
# check(Foo.xxx)  # xxx 函数


# 特点

# class Foo(object):
#     def f1(self):
#         pass
#
#     def f2(self):
#         pass
#
#     def f3(self):
#         pass
#
#     list_display = [f1, f2]
#
#     # def get_list_display(self):
#     #     self.list_display.append(self.f3)
#     #     return self.list_display
#
#     def __init__(self):
#         pass
#
#
# obj = Foo()
#
# Foo.list_display.append(obj.f3)
#
# for item in Foo.list_display:
#     print(item)  # 都是函数
#
#
# # 这里有一点，是否是函数还是方法，不是通过是否写在类里面判断的，而是通过调用这个函数的对象来判断的
# # 如果是通过类名来调用的，那么就是函数--就需要自己传递那个对象  如果是通过对象来调用的，那么就是方法--方法是自动传值的

# x1 = 123
#
#
# def f1(arg):
#     print(arg, 666)

# class Foo(object):
#     def __init__(self, a1):
#         self.a1 = a1
#
#
# obj = Foo(1)
#
# v1 = getattr(obj, "a1")
# print(v1)
#
# # # ！！!注意！:不推荐使用setattr
# # setattr(obj, "a2", 2)
# # v2 = getattr(obj, "a2")
# # print(v2)

def func():
    pass


class Foo(object):
    pass

    def func(self):
        pass


class Bar(object):
    def __call__(self, *args, **kwargs):
        pass


data = 123

obj = Foo()
obj1 = Bar()

print(callable(func))  # True
print(callable(Foo))  # True
print(callable(obj))  # False
print(callable(obj.func))  # True
print(callable(obj1))  # True
print(callable(data))  # False

# --END--
