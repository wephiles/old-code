# -*- coding: utf-8 -*-
# @CreateTime : 2024/5/26 026 15:46
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/demo7.py
# @Description : functools
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import functools


# 有时候会出现小bug
def auth(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        """
        inner函数
        Args:
            *args ():
            **kwargs ():

        Returns:
            返回值
        """
        res = func(*args, **kwargs)
        return res

    return inner


@auth
def admin():
    """
    这是admin函数。
    Returns:
        这是返回数据的注释
    """
    print(123)


@auth
def test():
    print("456")


# 执行: 函数名 + ()
admin()
print(admin.__name__)  # 输出这个函数的名称(字符串形式) admin
print(admin.__doc__)  # 输出这个函数的注释(字符串形式) 这个时候是admin的注释

test()
print(test.__name__)  # 输出这个函数的名称(字符串形式) test
print(test.__doc__)  # test的注释

# --END--
