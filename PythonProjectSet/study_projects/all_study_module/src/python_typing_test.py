#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime  :2024/09/04 21:37
# @Author      :wephiles@20866
# @IDE         :PyCharm
# @ProjectName :all_study_module
# @FileName    :all_study_module/python_typing_test.py
# @Description :This is description of this script.
# @Interpreter :Python 3.0+
# @Motto       :You must take your place in the circle of life!
# @AuthorSite  :https://github.com/wephiles or https://gitee.com/wephiles

# """
# Python类型注释、立即执行表达式.
# """
#
# from datetime import datetime
#
# var: str = 'hello'
#
#
# @lambda _: _()
# def func() -> str:
#     time_text: str = f'Start at {datetime.now():%H:%M:%S}'
#     print(time_text)
#     return time_text
#
#
# # 使函数像变量那样被使用
# x = func
# print(x)
# """
# Start at 21:50:23
# Start at 21:50:23
# """


# from datetime import datetime
# import time
#
# now = datetime.now()
# print(f'{now:%Y-%m-%d %H:%M:%S}')  # 2024-09-04 21:54:04
#
# print(time.strftime("%X (%d/%m/%Y)"))
# print(type(time.strftime("%X (%d/%m/%Y)")))  # str

# percent: float = 500.3751
# print(f'{percent:,.2%}')  # 50,037.51%

# people: dict = {'mario': 1, 'james': 2}
# print(people.get('mario111'))  # None
# print(people)  # {'mario': 1, 'james': 2}
#
# print(people.setdefault('asd', 0))  # 0
# print(people)  # {'mario': 1, 'james': 2, 'asd': 0}


# def analyse_text(text: str) -> dict:
#     details: dict = {
#         'words': (words := text.split()),
#         'amounts': len(words),
#         'chars': len(''.join(words)),
#         'reversed': words[::-1]
#     }
#     return details
#
#
# print(analyse_text('Hello world'))
#
# user_input: str = 'hell'
#
# if (text := len(user_input)) > 5:
#     print(text, '👍')
# else:
#     print(text, '👎')

# --END--
