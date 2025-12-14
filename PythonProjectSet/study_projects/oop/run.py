#!/user/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2024/11/22 19:18
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/run.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

class Foo:

    def __init__(self, name):
        self.name = name

    # 实例方法 -- 通过对象去调用
    def func(self):
        print(self.name)

    # 静态方法 -- 可以通过类去调用 -- 建议通过类调用
    @staticmethod
    def display():
        print(666)

    # 类方法
    @classmethod
    def show(cls, x):
        print(cls, x, 999)


Foo.show(18)

# --END--
