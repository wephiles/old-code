# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/24 024 18:46
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/demo1.py
# @Description : 创建三个学校，学校里面的设施内容是一样。
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

# class Message:
#     def __init__(self):
#         ...
#
#     def email(self, em, text):
#         """
#         发送邮件
#         Args:
#             em (str): 邮箱
#             text ():
#
#         Returns:
#
#         """
#         pass
#
#     def dingding(self, dingding, text):
#         """
#         发送钉钉消息
#         Args:
#             dingding (str): 钉钉号
#             text ():
#
#         Returns:
#
#         """
#         pass
#
#     def wechat(self, wechat, text):
#         """
#         发送微信消息
#         Args:
#             wechat (str): 微信号
#             text ():
#
#         Returns:
#
#         """
#         pass
#
#
# m1 = Message()
# m1.email('<EMAIL>', '')

# f = open("./db.txt", "r", encoding="utf-8")
# for line in f:
#     print(line.strip())
#
# f.close()

# def func(*args, **kwargs):
#     print(args)
#     print(kwargs["k1"])
#
#
# func(1, 2, 3, k1=1, k2=3)


# class Foo(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def func(self):
#         # 实例方法
#         print(self, "实例方法")
#         print(self.name)
#
#     @staticmethod
#     def display():
#         # 静态方法
#         print(123)
#
#     @classmethod
#     def show(cls, a, b):
#         """类方法"""
#         print(cls, 999)
#
#
# obj = Foo("computer")
# obj.func()
# obj.show(1, 2)  # cls传递的是当前类


# class Foo(object):
#     def __init__(self):
#         pass
#
#     @property
#     def start(self):
#         # 私有方法方法
#         return 1
#
#     @property
#     def end(self):
#         return 10
#
#
# obj = Foo()
# print(obj.start)
# print(obj.end)

class School(object):

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def speech(self):
        print("讲课")
        pass


obj1 = School("computer", "address-a")
obj2 = School("science", "address-b")
obj3 = School("technology", "address-c")


class Teacher(object):

    def __init__(self, name, age, __salary):
        self.name = name
        self.age = age
        self.__salary = __salary
        self.school = None


T1 = Teacher("a", 40, 15000)
T2 = Teacher("b", 64, 25000)
T3 = Teacher("c", 67, 35000)

T1.school = obj1
T2.school = obj1
T3.school = obj2

# 查看T1这个老师的学校的信息

print(T1.school.name)
print(T1.school.address)

# 查看老师的信息
print(T1.name)
print(T1.age)

T1.school.speech()

# --END--
