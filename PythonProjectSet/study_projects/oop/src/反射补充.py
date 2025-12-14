#!/user/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2024/12/17 20:03
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/反射补充.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# getattr()  # 根据字符串的形式去对象中找成员 - 内存级别
# hasattr()  # 根据字符串的形式判断对象中是否有该成员 - 内存级别
# setattr()  # 根据字符串的形式在对象中动态地设置一个成员 - 内存级别
# delattr()  # 根据字符串的形式去对象中动态地删除一个成员 - 内存级别

import handler

# print(hasattr(handler, 'f1'))  # True
# print(hasattr(handler, 'f3'))  # True
# print(hasattr(handler, 'func'))  # False

print(hasattr(handler, 'x2'))  # False
setattr(handler, 'x2', '666')
print(hasattr(handler, 'x2'))  # True

setattr(handler, 'x3', lambda x: x + 5)
print(getattr(handler, 'x3')(15))  # 20

print(hasattr(handler, 'x3'))  # True
delattr(handler, 'x3')
print(hasattr(handler, 'x3'))  # False

# --END--
