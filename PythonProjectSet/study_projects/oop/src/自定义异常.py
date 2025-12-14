#!/user/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2024/12/18 21:25
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/自定义异常.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles


class MyException(Exception):

    def __init__(self, code, message):
        self.code = code
        self.message = message


try:
    raise MyException(1000, 'Error')
except MyException as e:
    print(e.code)
    print(e.message)

# --END--
