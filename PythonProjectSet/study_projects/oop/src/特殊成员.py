#!/user/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2024/12/14 13:01
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/特殊成员.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# class Foo(object):
# 
#     def __new__(cls, *args, **kwargs):  # 构造方法
#         print('__new__方法', cls)
#         # __new__的时候创建一个空对象。
#         # 将object.__new__(cls)返回后就回去调用__init__方法，初始化对象
# 
#         # 必须要有返回值且返回值必须是object.__new__(cls)
#         # 所有的对象都是由object创建的
#         return object.__new__(cls)
# 
#     def __init__(self, a1, a2):  # 初始化方法
#         self.a1 = a1
#         self.a2 = a2
#         print('__init__方法')
# 
#     def __call__(self, *args, **kwargs):
#         print(111, args, kwargs)
#         return 123
# 
#     def __getitem__(self, name):
#         return 8
# 
#     def __setitem__(self, name, value):  # 无返回值
#         print('key', 'value', name, value)
# 
#     def __delitem__(self, name):  # 无返回值
#         print('del', name)
# 
# 
# # 1. 类名() -- 自动执行__init__方法
# obj = Foo(1, 2)
# 
# # 2. 对象() -- 自动执行 __call__方法
# obj(1, 2, k1=10, k2=20)
# 
# # 3. 对象[] -- 自动执行 __getitem__方法
# print(obj['xx'])
# 
# # 4. 对象[a] = b -- 自动执行 __setitem__方法
# obj['abc'] = 123
# 
# # 5. del 对象[a] -- 自动执行 __delitem__方法
# del obj['123']
# 
# # 6. __new__方法 -- 真正的构造方法

# class Foo(object):
#     """This is a class docstring."""
#     def __init__(self):
#         pass
#
#     def func(self):
#         pass
#
#     def __str__(self):
#         return "A object from Foo class."
#
#
# obj = Foo()
# print(obj)
# print(obj.__doc__)  # This is a class docstring.

class Foo(object):
    """This is a class docstring."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.detail = [(1, 5), (2, 6), (3, 7)]

    def __iter__(self):
        return iter(self.detail)


obj = Foo('aaa', 123)

for item in obj:
    print(item)
"""
(1, 5)
(2, 6)
(3, 7)
"""

# --END--
