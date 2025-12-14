#!/user/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2024/12/14 12:43
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/主动调用其他类的成员.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles


class Foo(object):

    def f1(self):
        super().f1()  # 按照继承顺序找下一个类的相关成员
        print('Foo.f1 3个功能')


class Bar(object):

    def f1(self):
        print('Bar.f1 6个功能')


class Info(Foo, Bar):
    pass


obj = Info()
obj.f1()

"""
Bar.f1 6个功能
Foo.f1 3个功能

！！！
Info没有f1，先去Foo里面找(先找左边)，找到了，执行Foo.f1函数
在执行Foo.f1函数的时候，这个函数的第一条语句需要按照继承关系找函数，
但是是按照哪个类的继承关系找呢？是按照Info类还是Foo类呢？答案是：按照Info的
继承关系去找。因为最开始是按照Info的继承关系找f1函数，那么传入的self参数肯定就只是
Info的对象obj这个对象了。
==========================================================================
总结一下，如果要执行/找到一个对象的成员，那么从始至终必须要按照这个对象的继承关系去
找。不能找到一半又去不是下一个继承关系的类里面找。并不是简单的找父类。 -- 易错点
！！！
"""

# --END--
