#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime  :2024/09/04 21:15
# @Author      :wephiles@20866
# @IDE         :PyCharm
# @ProjectName :all_study_module
# @FileName    :all_study_module/test_protocols.py
# @Description :This is description of this script.
# @Interpreter :Python 3.0+
# @Motto       :You must take your place in the circle of life!
# @AuthorSite  :https://github.com/wephiles or https://gitee.com/wephiles

from typing import Protocol


class Printable(Protocol):
    pages: int

    def print_item(self):
        pass

    def recycle(self):
        pass


class Book:
    pages: int

    def __init__(self, title: str):
        self.title = title

    def print_item(self):
        print(f'Printing: {self.title}')

    def recycle(self):
        print(f'Recycling: {self.title}')


class Magzaine:
    def __init__(self, title: str):
        self.title = title


def print_printable(printable: Printable):
    printable.print_item()


book = Book('三国演义')
print_printable(book)

magazine: Printable = Magzaine('读者')
print_printable(magazine)  # 报错 除非实现协议类Printable所实现的所有方法和变量

# --END--
