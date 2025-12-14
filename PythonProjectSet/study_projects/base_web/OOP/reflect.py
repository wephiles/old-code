# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/27 027 18:32
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/reflect.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

# import handler
# from types import FunctionType
#
# # handler.f1()
# # handler.f2()
# # handler.f3()
# # handler.f4()
# # handler.f5()
#
# print("""系统支持的函数有:
#     1: f1
#     2: f2
#     3: f3
#     4: f4
#     5: f5
# """, end=" ")
#
# while True:
#     print("请输入要执行的函数. eg: \n>>>f1 \n ===================================")
#     val = input(">>> ")
#     # handler.val()  # 错误的写法 -- 因为这样会去handler里面找val函数！但是handler里面没有这个函数，
#     # 此外，如果有这个函数的话，可能造成巨大的问题！
#
#     # # 下面这样写是正确的，但是不够优雅！！！
#     # if var == "f1":
#     #     handler.f1()
#     # elif var == "f2":
#     #     handler.f2()
#     # elif var == "f3":
#     #     handler.f3()
#     # elif var == "f4":
#     #     handler.f4()
#     # elif var == "f5":
#     #     handler.f5()
#     # else:
#     #     print("输入错误, 请重新输入.")
#
#     # # 怎么办？ -- 使用反射！
#     # # 反射：通过字符串调用函数，而不是直接调用函数。
#     # func = getattr(handler, "f1")  # 直接去handler模块里面找f1函数(通过字符串的形式) -- 返回一个function对象
#     # func()
#     # # 这个函数的作用是通过字符串调用函数，而不是直接调用函数。
#     # # 第一个参数是模块名，第二个参数是函数名(字符串类型)。
#     # # 它会返回一个函数对象，然后就可以调用这个函数对象了。
#     if hasattr(handler, val):
#         func_or_val = getattr(handler, val)
#         if isinstance(func_or_val, FunctionType):
#             func_or_val()
#         else:
#             print(func_or_val)
#     else:
#         print("输入错误, 请重新输入.")
#         break
#
#     # 这样就可以通过字符串调用函数了！

# class Foo(object):
#     country = "中国"
#
#     def func(self):
#         pass


# v = getattr(Foo, "country")  # 根据字符串，从类实例中寻找
# print(v)  # 中国

# v = getattr(Foo, "func")  # # 根据字符串，从类中寻找
# print(v)  # <function Foo.func at 0x0000027D372D8C20>

# obj = Foo()
#
# v = getattr(obj, "func")  # 根据字符串，从对象中寻找
# print(v)  # <bound method Foo.func of <__main__.Foo object at 0x000001EEE8031550>>
# class Foo(object):
#     country = "中国"
#
#     def func(self):
#         pass


# v = getattr(Foo, "country")  # 根据字符串，从类实例中寻找
# print(v)  # 中国

# v = getattr(Foo, "func")  # # 根据字符串，从类中寻找
# print(v)  # <function Foo.func at 0x0000027D372D8C20>

# obj = Foo()
#
# v = getattr(obj, "func")  # 根据字符串，从对象中寻找
# print(v)  # <bound method Foo.func of <__main__.Foo object at 0x000001EEE8031550>>
# --END--
