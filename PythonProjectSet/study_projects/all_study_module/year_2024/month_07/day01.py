# -*- coding: utf-8 -*-
# @CreateTime : 2024/7/1 001 21:44
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : all_study_module
# @FileName : all_study_module/day01.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

# from typing import TypeAlias, Literal, NewType

# TypeAlias:
# # 类型定义别名的直接方法
# my_type = tuple[int, str]
# var: my_type = (10, 10)
#
# print(var)  # (10, 10)

# Strings: TypeAlias = list[str]
#
# # people: Strings = ['computer', 'science']
# people: Strings = [10, 10]
# print(people)

# Basket: TypeAlias = 'list[Fruit]'
#
#
# class Fruit(object):
#     def __init__(self, fruit):
#         self.fruit = fruit
#
#     def create_basket(self) -> Basket:
#         return 3 * [Fruit(self.fruit)]
#
#
# banana: Fruit = Fruit('Banana')
# basket: Basket = banana.create_basket()
# print(basket[0].fruit)

# Literal:

# Mode: TypeAlias = Literal['r', 'w', 'a']
#
#
# def open_file(file: str, mode: Mode) -> str:
#     return f'Reading {file} in "{mode}" mode.'
#
#
# print(open_file('test.txt', 'r'))
# print(open_file('test.txt', 'a'))
# print(open_file('test.txt', 'w'))

# NewType

# UserId = NewType('UserId', int)
# print(UserId(10))  # 10
#
#
# def find_user(user_id: UserId) -> int:
#     print('Found:', user_id)
#
#
# find_user(UserId(100))

# def hidden_feature_1(a, b, *args, **kwargs):
#     print('a =', a, ',b =', b, ',args =', args, ',kwargs =', kwargs)
#
#
# hidden_feature_1('12', 22, 'hello', 'world', c=13, d=456, e=[12, 34, 56])
# # a = 12 ,b = 22 ,args = ('hello', 'world') ,kwargs = {'c': 13, 'd': 456, 'e': [12, 34, 56]}

# def function_caller(func, *args, **kwargs):
#     return func(*args, **kwargs)
#
#
# def add(a, b):
#     return a + b
#
#
# def pow_cal(base=1, exp=1):
#     return base ** exp
#
#
# res = function_caller(add, 2, 3)
# print(res)
#
# res = function_caller(pow_cal, base=2, exp=3)
# print(res)
#
# funcs = [add, pow_cal, add, add]
# args = [
#     [(1, 2), {}],
#     [(), {"base": 5, "exp": 2}],
#     [(5, 6), {}],
#     [(3, 4), {}]
# ]
#
# for func, (args, kwargs) in zip(funcs, args):
#     res = func(*args, **kwargs)
#     print(res)

# 闭包
# def adder(value):
#     def inner(base):
#         return base + value
#
#     return inner
#
#
# add_5 = adder(5)
# add_10 = adder(10)
#
# res = add_5(11)
# res_1 = add_5(-7)
# res_2 = add_10(100)
#
# print(res)
# print(res_1)
# print(res_2)


# 装饰器 -- 修改另一个函数的函数
# def func_printer(func):
#     def modified_func(*args, **kwargs):
#         print(f'Functions called with {args} and {kwargs}.')
#         result = func(*args, **kwargs)
#         print(f'Result is {result}')
#         return result
#
#     return modified_func
#
#
# @func_printer
# def my_function(list1, list2, mod=1):
#     new_list = []
#
#     for lst in [list1, list2]:
#         for value in lst:
#             if value % mod == 0:
#                 new_list.append(value)
#
#     return new_list
#
#
# my_function([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], mod=2)
#
# # # 下面这两行就是装饰器的内在逻辑 等价于在定义函数的时候写上@func_printer,
# # # 再调用函数my_function([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], mod=2)
# #
# # my_function = func_printer(my_function)
# # my_function([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], mod=2)

# # 非本地关键字 可以在内部函数中修改外部函数的变量
# # 需要注意的是，nonlocal 关键字只能在嵌套函数中使用，而不能在全局作用域中使用。它用于解决内部函数无法直接访问外部函数的变量的问题。
# # 注意，global只能在函数内申明位于模块的关键字 -- 不在任何函数内的关键字叫位于模块内的关键字（我发明的，不知对不对，但大概就是这个意思）
# # def outer():
# #     x = 10
# #
# #     def inner():
# #         x = 20
# #         print('Inner x:', x)
# #
# #     inner()
# #     print('Outer x:', x)
# #
# #
# # outer()
# # # inner x: 20
# # # Outer x: 10
#
# def outer():
#     x = 10
#
#     def inner():
#         nonlocal x
#         x = 20
#         print('Inner x:', x)
#
#         def inner_2():
#             nonlocal x
#             x = 100
#             print('inner inner:', x)
#
#         inner_2()
#
#     inner()
#     print('Outer x:', x)
#
#
# outer()
# # Inner x: 20
# # inner inner: 100
# # Outer x: 100

# from typing import List, Tuple, Optional
#
#
# def greet(name: str) -> str:
#     return f'Hello {name}'
#
#
# def add(x: int, y: int) -> int:
#     return x + y
#
#
# def process_data(data: List[int]) -> Tuple[int, int]:
#     return min(data), max(data)
#
#
# def find_max(data: Optional[List[int]] = None) -> Optional[int]:
#     if data:
#         return max(data)
#
#     return None
#
#
# print(process_data([1, 2, 3]))

# import time
# from itertools import cycle
#
# lights = [
#     ("Green", 2),
#     ("Yellow", 0.5),
#     ("Red", 2)
# ]
#
# # i = 0
# # while True:
# #     c, s = lights[i]
# #     print(c)
# #     time.sleep(s)
# #     if i == len(lights) - 1:
# #         i = 0
# #     else:
# #         i += 1
#
# colors = cycle(lights)
# while True:
#     c, s = next(colors)
#     print(c)
#     time.sleep(s)

# # 列表解析
#
# names = [
#     'Rick C. Brown',
#     'Rick D. Green',
#     'Rick E. Smith',
#     'Rick F. Davis'
# ]
#
# last = [n.split(' ')[-1].strip() for n in names]
# print(last)

# 解包

# inputs = [
#     'John',
#     'Smith',
#     'American',
#     'Blue',
#     'Brown',
#     29
# ]
#
# first_name, last_name, *_, age = inputs
# print(first_name, last_name, age)

# names = [
#     'Rick C. Brown',
#     'Rick D. Green',
#     'Rick E Smith',
#     'Rick F Davis'
# ]
#
# dict_name_len = {name: len(name) for name in names}
# print(dict_name_len)

# func = lambda x, y: x + y
#
# x = func(1, 2)
# print(x)


# balance = 1254.25
#
# while True:
#     try:
#         num = float(input("Deposit: "))
#         break
#     except ValueError:
#         print("Please input the correct number:")
# balance += num
# print(balance)


# def do_this():
#     print('doing this.')
#
#
# def do_that():
#     print('doing that.')
#
#
# match input('do this or that:'):
#     case 'this':
#         do_this()
#     case 'that':
#         do_that()
#     case _:
#         print('I did not understand')

# global_var = 10
#
#
# def func():
#     ans = 0
#     local_var = global_var
#     for i in range(1000):
#         ans += local_var * i
#     return ans
#
#
# x = func()
# print(x)

# a = [1, 2, 3, 3, 4, 5, 6]
# b = [4, 5, 5, 6, 7, 8, 9]
# 
# 
# # 合并在一起 去除重复项
# 
# def merge(list1, list2):
#     return sorted((set(list1 + list2)))
# 
# 
# x = merge(a, b)
# print(x)

# a = [1, 2, 5, 1, 3, 3, 5, 8]
# new_dict = dict.fromkeys(a)
# print(list(new_dict))

# from module import connect
#
# # print(__name__)
#
# if __name__ == '__main__':
#     connect()

# def greet() -> None:
#     print('Hello, world!')
#
#
# def bye() -> None:
#     print('Bye, world!')
#
#
# def main() -> None:
#     greet()
#     bye()
#
#
# if __name__ == '__main__':
#     main()

# def is_adult(age: int, has_id: bool) -> bool:
#     return age >= 21 and has_id
#
#
# def is_bob(name: str) -> bool:
#     return name.lower() == 'bob'
#
#
# def enter_club(name: str, age: int, has_id: bool) -> None:
#     # if name.lower() == 'bob':
#     #     print('Get out of here Bob, we do not want no trouble.')
#     #     return
#     #
#     # if age > 21 and has_id:
#     #     print('You may enter the club.')
#     # else:
#     #     print('You may not enter the club.')
#
#     # 上述这个实现不好 -- 应该抽象出来一些东西
#     if is_bob(name):
#         print('Get out of here Bob, we do not want no trouble.')
#         return
#
#     if is_adult(age, has_id):
#         print('You may enter the club.')
#     else:
#         print('You may not enter the club.')
#
#
# def main() -> None:
#     enter_club('Bob', 29, has_id=True)
#     enter_club('James', 29, has_id=True)
#     enter_club('Green', 29, has_id=False)
#     enter_club('Mario', 29, has_id=True)
#
#
# if __name__ == '__main__':
#     main()

# number: int = 10
#
#
# def upper_everything(elements: list[str]) -> list[str]:
#     """
#     多余的文档注释是坏事！
#     Args:
#         elements ():
#
#     Returns:
#
#     """
#     return [element.upper() for element in elements]
#
#
# loud_list: list[str] = upper_everything(['Computer', 'Science'])
#
#
# # 下面这个明显有错误 但是pycharm竟然不会显示警告信息
# sample: list[int] = ['a', 1, 'b', 2]
#
# # 方法：使用mypy -- pip install mypy
# # 这样类似于上面的代码就会导致pycharm警告产生

names: list[str] = ['James', 'Charlotte', 'Stephany', 'Mario', 'Sandra']

# for person in people:
#     if len(person) > 7:
#         long_names.append(person)
# 上面这三行代码可以使用一行代码代替：
long_names: list[str] = [name for name in names if len(name) > 7]

print(f"Long names: {long_names}")

# # 你甚至可以：
# print(f"Long names: {[item for item in people if len(item) > 7]}")

# --END--
