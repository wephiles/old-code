#!/user/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2024/12/08 15:07
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/组合02.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles


"""对象中到底有什么"""


class Foo(object):

    def __init__(self, age):
        self.age = age

    def display(self):
        print(self.age)


data_list = [Foo(10), Foo(11), Foo(12), Foo(13)]

for item in data_list:
    print(item.age, item.display())

"""
10
10 None
11
11 None
12
12 None
13
13 None
"""

# --END--
