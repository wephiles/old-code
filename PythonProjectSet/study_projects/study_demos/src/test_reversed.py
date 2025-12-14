#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime  :2024/09/03 22:21
# @Author      :wephiles@20866
# @IDE         :PyCharm
# @ProjectName :study_demos
# @FileName    :study_demos/test_reversed.py
# @Description :This is description of this script.
# @Interpreter :Python 3.0+
# @Motto       :You must take your place in the circle of life!
# @AuthorSite  :https://github.com/wephiles or https://gitee.com/wephiles

"""
The purpose of this file is to test the functions called reversed.
"""

from sys import getsizeof
from typing import Any


def display_info(var: Any):
    print(f'{var} ({getsizeof(var)} bytes)')


text: str = 'Python language'
coordinates: list[str] = ['a1', 'b2', 'c3', 'd4', 'e5', 'f6']

display_info(text[::-1])
display_info(coordinates[::-1])
# egaugnal nohtyP (56 bytes)
# ['f6', 'e5', 'd4', 'c3', 'b2', 'a1'] (104 bytes)

print(reversed(text))  # <reversed object at 0x000001AF54144280>

reversed_text = reversed(text)
reversed_coordinates = reversed(coordinates)
display_info(reversed_text)  # 实际上是生成了一个生成器 -- 节省内存
display_info(reversed_coordinates)  # 实际上是生成了一个生成器 -- 节省内存
# <reversed object at 0x000001E6E9074400> (48 bytes)
# <list_reverseiterator object at 0x000001E6E9075600> (48 bytes)


display_info(''.join(reversed_text))  # egaugnal nohtyP (56 bytes)

display_info(list(reversed_coordinates))
# ['f6', 'e5', 'd4', 'c3', 'b2', 'a1'] (104 bytes)

# --END--
