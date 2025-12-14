#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime  :2024/09/02 18:48
# @Author      :wephiles@20866
# @IDE         :PyCharm
# @ProjectName :study_demos
# @FileName    :study_demos/test_typing.py
# @Description :This is description of this script.
# @Interpreter :Python 3.0+
# @Motto       :You must take your place in the circle of life!
# @AuthorSite  :https://github.com/wephiles or https://gitee.com/wephiles


from typing import TypeAlias
from typing import Literal

# my_type = tuple[int, str]
#
# var: my_type = (10, '10')
#
# print(var)

# Strings: TypeAlias = list[str]
# # people: Strings = ['James', 'Mario']
# people: Strings = [10, 10]
# print(people)

# # 前向引用
# Basket: TypeAlias = 'list[Fruit]'
#
#
# class Fruit(object):
#     def __init__(self, fruit: str) -> None:
#         self.fruit = fruit
#
#     def create_basket(self) -> Basket:
#         return 3 * [Fruit(self.fruit)]
#
#
# banana: Fruit = Fruit('banana')
# basket: Basket = banana.create_basket()
#
# print(basket[0].fruit)


# Mode: TypeAlias = Literal['r', 'w', 'a']
#
#
# def open_file(file: str, mode: Mode) -> str:
#     return 'reading {} with mode {}'.format(file, mode)
#
#
# print(open_file('indently.txt', 'a'))  # reading indently.txt with mode a
# print(open_file('indently.txt', 'T'))  # reading indently.txt with mode T 但是IDE会提示错误

# Age: TypeAlias = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def send(age: Age):
#     print(age)
#
#
# send(1000)

# from typing import NewType
# from typing import Dict
#
# a: Dict[int, int] = {10: 10}
# print(a)

from typing import NewType

UserId = NewType('UserId', int)


def find_user(user_id: UserId):
    print(user_id)


find_user(UserId(10))  # IDE提示: Expected type 'UserId', got 'int' instead

# print(UserId)

# from typing import Union, Any, Optional
#
#
# def my_func(arg: Union[str, int]) -> Optional[int]:
#     print(arg)
#     return 0
#
#
# my_func(20)

# --END--
