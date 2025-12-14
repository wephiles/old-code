# -*- coding: utf-8 -*-
# @CreateTime : 2024/5/26 026 15:24
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/demo5.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

def outer(origin):
    def inner(*args, **kwargs):
        print("before")
        # 定义函数的时候可以*args, **kwargs，执行函数的时候也可以*args, **kwargs
        result = origin(*args, **kwargs)
        print("after")
        return result

    return inner


@outer
def func(a):
    print("i am func function")
    value = (1, 2, 3, 4)
    return value


@outer
def func1(a1, a2):
    print("i am func1 function")
    value = (11, 12, 13, 14)
    return value


@outer
def func2(a):
    print("i am func2 function")
    value = (21, 22, 23, 24)
    return value


# func = outer(func)

print(func(1))
print(func1(1, 2))
print(func2(2))

# --END--
