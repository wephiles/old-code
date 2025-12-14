#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime  :2024/09/04 19:16
# @Author      :wephiles@20866
# @IDE         :PyCharm
# @ProjectName :all_study_module
# @FileName    :all_study_module/test_script.py
# @Description :This is description of this script.
# @Interpreter :Python 3.0+
# @Motto       :You must take your place in the circle of life!
# @AuthorSite  :https://github.com/wephiles or https://gitee.com/wephiles

# import secrets
# import string
#
# random = secrets.randbelow(10)  # [0 , 10)
# print(random)
#
# random_choice = secrets.choice([11, 12, 13, 14, 15, 16, 17, 18, 19])
# print(random_choice)
#
#
# def generate_password(length: int):
#     chars: str = string.ascii_letters + string.digits + string.punctuation
#     # 字母 + 数字 + 标点符号
#     password: str = ''.join(secrets.choice(chars) for i in range(length))
#     print(f'Generated password:"{password}"')
#
#
# generate_password(18)

# ============================================================================
# random = secrets.randbits(2)
# print(random)

# ============================================================================

# token = secrets.token_bytes(32)
# token_1 = secrets.token_hex(32)
# print(token)
# print(token_1)

# ============================================================================
# token = secrets.token_urlsafe(32)
# print(f'https://www.website.com/authenticate/{token}')

# ============================================================================
# user_input = 'abc123'
# password = 'abc123'
# if secrets.compare_digest(user_input, password):
#     print('Password match!')

# ============================================================================

# sr = secrets.SystemRandom()
# sr.choice()
# sr.random()
# ...

# class Test:
#     def __new__(cls, *args, **kwargs):
#         pass
#
#     def __init__(self):
#         pass


# class Connection:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             print('Connecting internet ...')
#             cls.__instance = super().__new__(cls)
#             # 必须要有返回值
#             return cls.__instance
#         else:
#             print('Warning: There is already an instance of connection!')
#             return cls.__instance
#
#     def __init__(self):
#         print('Connected to the internet.')
#
#
# connection = Connection()
# connection1 = Connection()
#
# print(connection == connection1)  # True

# ============================================================================

# class Vehicle:
#
#     def __new__(cls, wheels: int):
#         if wheels == 2:
#             return MotorBike()
#         elif wheels == 4:
#             return Car()
#         else:
#             return super().__new__(cls)
#
#     def __init__(self, wheels: int):
#         self.wheels = wheels
#         print(f'Initializing vehicle with {wheels} wheels.')
#
#
# class MotorBike:
#     def __init__(self):
#         print('Initializing motorbike.')
#
#
# class Car:
#     def __init__(self):
#         print('Initializing car.')
#
#
# B = Vehicle(2)
# C = Vehicle(4)
# bus = Vehicle(20)

# ============================================================================

# import sys
#
# print(sys.version_info > (3, 10))


# from enum import Enum
# from http import HTTPStatus
#
#
# class Status(Enum):
#     OK = 200
#     BAD_GATEWAY = 502
#     FORBIDDEN = 403
#
#
# status = Status.FORBIDDEN
#
# # if status == Status.FORBIDDEN:
# #     print('Forbidden')
#
# # 上述实现有点慢 下面看快的
#
# # from http import HTTPStatus
#
# print(HTTPStatus.OK)
# print(HTTPStatus.OK.phrase)
# print(HTTPStatus.OK.description)
# """Result:
# HTTPStatus.OK
# OK
# Request fulfilled, document follows
# """
#
# print(HTTPStatus.TOO_MANY_REQUESTS)
# print(HTTPStatus.TOO_MANY_REQUESTS.phrase)
# print(HTTPStatus.TOO_MANY_REQUESTS.description)
# """Result:
# HTTPStatus.TOO_MANY_REQUESTS
# Too Many Requests
# The user has sent too many requests in a given amount of time ("rate limiting")
# """
#
# print(HTTPStatus.IM_A_TEAPOT)
# print(HTTPStatus.IM_A_TEAPOT.phrase)
# print(HTTPStatus.IM_A_TEAPOT.description)
# """Result:
# HTTPStatus.IM_A_TEAPOT
# I'm a Teapot
# Server refuses to brew coffee because it is a teapot.
# """

# ============================================================================

# import __hello__
#
# __hello__.main()

# source: str = 'str(10 * 10 + 2) + "hello"'
#
# res: str = eval(source)
# print(res)  # 102hello

# source: str = '''
# print("exec():")
# x = 10
# y = 11
#
# for i in range(3):
#     print(x + y, i, sep='-')
# '''
#
# exec(source)
# """Result:
# exec():
# 21-0
# 21-1
# 21-2
# """


# def multiply_setup(a: float):
#     def multiply(b: float):
#         return a * b
#
#     return multiply
#
#
# double = multiply_setup(2)
# triple = multiply_setup(3)
#
# print(double(10))  # 20
# print(triple(5))  # 15

# from functools import partial
#
#
# def multiply(a: float, b: float, name: str | None = None) -> float:
#     if name:
#         print(f'{name} (a: {a}, b: {b})')
#     return a * b
#
#
# double = partial(multiply, 2, name='double')
# triple = partial(multiply, b=3, name='triple')
# print(double(10))  # 20
# print(triple(10))  # 30
#
# """Result:
# double (a: 2, b: 10)
# 20
# triple (a: 10, b: 3)
# 30
# """


# import antigravity

# def chunks(lst: list, n: int):
#     for i in range(0, len(lst), n):
#         yield lst[i:i + n]
#
#
# x = chunks(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 2)
# for item in x:
#     print(item)

# from uuid import uuid4
#
#
# class User:
#     def __init__(self):
#         self._uid = uuid4()
#
#     def _get_id(self):
#         return self._uid
#
#
# user = User()
# id_ = user._get_id()  # 报警告 但是可以获取值
# print(id_)  # 838ef4e4-d1ce-4eec-877e-7574972c74f1

# --END--
