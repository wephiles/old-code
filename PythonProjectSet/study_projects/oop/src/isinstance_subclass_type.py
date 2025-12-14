#!/user/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2024/12/15 16:27
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/isinstance_subclass_type.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles


from types import MethodType, FunctionType


class Foo(object):
    def f1(self):
        pass

    def f2(self):
        pass

    list_display = [f1, f2]

    def get_list_display(self):
        self.list_display.append(self.f3)
        return self.list_display

    def f3(self):
        pass

    def __init__(self):
        pass


obj = Foo()
obj.get_list_display()
for item in obj.list_display:
    print(item)

for item in Foo.list_display:
    print(item)

"""
<function Foo.f1 at 0x000001C41C0D1750>
<function Foo.f2 at 0x000001C41C0D16C0>
<bound method Foo.f3 of <__main__.Foo object at 0x000001C41DD13FD0>>
<function Foo.f1 at 0x000001C41C0D1750>
<function Foo.f2 at 0x000001C41C0D16C0>
<bound method Foo.f3 of <__main__.Foo object at 0x000001C41DD13FD0>>
"""

# def if_func(arg):
#     if isinstance(arg, MethodType):
#         print('方法')
#     if isinstance(arg, FunctionType):
#         print('函数')


# --END--
