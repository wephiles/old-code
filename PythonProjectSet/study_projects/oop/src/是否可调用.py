#!/user/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2024/12/17 20:27
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/是否可调用.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

def func():
    pass


class Foo(object):
    def __call__(self):
        pass


obj = Foo()

print(callable(func))
print(callable(Foo))
print(callable(obj))

"""
True
True
True
"""

# --END--
