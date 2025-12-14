#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime  :2024/09/03 21:59
# @Author      :wephiles@20866
# @IDE         :PyCharm
# @ProjectName :study_demos
# @FileName    :study_demos/test_reduce.py
# @Description :This is description of this script.
# @Interpreter :Python 3.0+
# @Motto       :You must take your place in the circle of life!
# @AuthorSite  :https://github.com/wephiles or https://gitee.com/wephiles

"""
This file learn how to user reduce! Maybe.

reduce: 将列表或者可迭代元素转换成单个元素。
"""

from functools import reduce

numbers: list[int] = [1, 2, 3, 4, 5, 6]
result: float = reduce(lambda a, b: a * b, numbers)
# arguments :func, sequence and init_value
print(result)  # 720 = ((((1*2)*3)*4)*5)*6

string: list[str] = ['a1', 'b2', 'c3', 'd4', 'e5', 'f6']
# Attention: the first argument func can only receive two arguments!
# About the third argument:
#   if the sequence list is None, it will print the third argument also!
# Attention: But if the length of the sequence list equals one,
# then it will only print the only element of the list,
# do not print the third argument!!!
result: str = reduce(lambda a, b: f'{a}-{b}', string, 'Init')
print(result)  # Init-a1-b2-c3-d4-e5-f6

# --END--
