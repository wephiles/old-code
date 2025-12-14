#!/user/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2024/12/17 19:37
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/反射.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

import handler

while True:
    print('系统支持的函数有: \n1. f1 \n2. f2 \n3. f3 \n4. f4 \n5. f5')
    val = input('请输入要执行的函数:')
    if val in ('f1', 'f2', 'f3', 'f4', 'f5'):
        getattr(handler, val)()
    else:
        break

# --END--
