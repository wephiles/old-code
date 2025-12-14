#!/user/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2024/12/08 15:03
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/组合01.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

"""类 / 对象能否做字典的key"""


class Foo(object):

    def __init__(self):
        pass


obj = Foo()

my_dict = {
    Foo: 12,
    obj: 123,
}

for key, value in my_dict.items():
    print(key, value)

# --END--
