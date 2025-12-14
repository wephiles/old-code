# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/26 026 21:44
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/practice.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

# class StarkConfig(object):
#     list_display = []
#
#     def __init__(self):
#         pass
#
#     def get_list_display(self):
#         self.list_display.insert(0, 3)
#         return self.list_display
#
#
# class RoleConfig(object):
#     list_display = [11, 22]
#
#     def __init__(self):
#         pass
#
#
# s1 = StarkConfig()
#
# res1 = s1.get_list_display()
# print(res1)
#
# res2 = s1.get_list_display()
# print(res2)


# class StarkConfig(object):
#     list_display = []
#
#     def __init__(self):
#         pass
#
#     def get_list_display(self):
#         self.list_display.insert(0, 3)
#         return self.list_display
#
#
# class RoleConfig(object):
#     list_display = [11, 22]
#
#     def __init__(self):
#         pass
#
#
# s1 = RoleConfig()
# s2 = RoleConfig()
#
# res1 = s1.get_list_display()
# print(res1)
#
# res2 = s2.get_list_display()
# print(res2)


# class StarkConfig(object):
#     list_display = []
#
#     def __init__(self):
#         pass
#
#     def get_list_display(self):
#         self.list_display.insert(0, 3)
#         return self.list_display
#
#
# class RoleConfig(object):
#     list_display = [11, 22]
#
#     def __init__(self):
#         pass
#
#
# s1 = RoleConfig()
# s2 = RoleConfig()
#
# res1 = s1.get_list_display()
# print(res1)  # 报错
#
# res2 = s2.get_list_display()
# print(res2)  # 报错

# class StarkConfig(object):
#     list_display = []
#
#     def __init__(self):
#         pass
#
#     def get_list_display(self):
#         self.list_display.insert(0, 3)
#         return self.list_display
#
#
# class RoleConfig(StarkConfig):
#     list_display = [11, 22]
#
#     def __init__(self):
#         pass
#
#
# s1 = StarkConfig()
# s2 = RoleConfig()
#
# res1 = s1.get_list_display()
# print(res1)  # [3]
#
# res2 = s2.get_list_display()
# print(res2)  # [3, 11, 22]

# class StarkConfig(object):
#     list_display = []
#
#     def __init__(self):
#         pass
#
#     def get_list_display(self):
#         self.list_display.insert(0, 3)
#         return self.list_display
#
#
# class RoleConfig(StarkConfig):
#     list_display = [11, 22]
#
#     def __init__(self):
#         pass
#
#
# s1 = RoleConfig()
# s2 = RoleConfig()
#
# res1 = s1.get_list_display()
# print(res1)  # [3, 11, 22]
#
# res2 = s2.get_list_display()
# print(res2)  # [3, 3, 11, 22]

# class Account(object):
#     function_list = ['login', 'register', 'logout']
#
#     def login(self):
#         """
#         登录
#         Returns:
#
#         """
#         print("login")
#
#     def register(self):
#         """
#         注册
#         Returns:
#
#         """
#         print("register")
#
#     def logout(self):
#         """
#         注销
#         Returns:
#
#         """
#         print('logout')
#
#     def run(self):
#         """
#         运行 主代码
#         Returns:
#
#         """
#
#         print("请输入要执行的功能：1、登录 2、注册 3、注销 4、退出")
#         choice = int(input(">>> "))
#         func_name = Account.function_list[choice - 1]
#         # func = getattr(Account, func_name)  # 函数
#         # func(self)
#         func = getattr(self, func_name)  # 函数
#         func()
#         pass
#
#
# obj = Account()
# obj.run()
#
# obj1 = Account()
# obj1.run()


import demo3

v1 = (demo3, "x1")
v2 = getattr(demo3, "f1")

# # getattr
# print(v1)  # (<module 'demo3' from 'F:\\CSProjects\\PycharmProjects\\studyProject\\OOP\\demo3.py'>, 'x1')
# print(v2)  # <function f1 at 0x000002CCD1998C20>
# v2("computer")  # computer 666

# hasattr
v3 = hasattr(demo3, "x1")
v4 = hasattr(demo3, "f1")
v5 = hasattr(demo3, "f111")
print(v3, v4)  # True True
print(v5)  # False

# setattr
setattr(demo3, 'x2', 999)  # 设置了 但demo3.py中没有x2 -- 在内存中 但是没有写入文件
print(getattr(demo3, 'x2'))  # 999

setattr(demo3, 'f2', lambda x: x + 1)  # 设置了 但demo3.py中没有x2 -- 在内存中 但是没有写入文件
print(getattr(demo3, 'f2'))  # <function <lambda> at 0x000001F6DCCBE0C0>

# delattr

delattr(demo3, "x1")
v9 = getattr(demo3, "x1")  # 报错

# --END--
