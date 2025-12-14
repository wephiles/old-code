#!/user/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2024/12/17 19:49
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/反射1.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

"""
反射 -- 通过面向对象实现
"""


class Foo(object):
    country = 'a'

    def func(self):
        pass


v = getattr(Foo, 'country')
print(v)

v = getattr(Foo, 'func')
print(v)

obj = Foo()
v = getattr(obj, 'func')
print(v)

"""
a
<function Foo.func at 0x00000200233C1750>
<bound method Foo.func of <__main__.Foo object at 0x0000020025013FA0>>
"""


def function():
    name = 'abc'


v = getattr(function, 'name')
print(v)  # 报错 AttributeError: 'function' object has no attribute 'name'

# --END--
