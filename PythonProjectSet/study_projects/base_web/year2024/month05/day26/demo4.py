# -*- coding: utf-8 -*-
# @CreateTime : 2024/5/26 026 15:19
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/demo4.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

def outer(origin):
    def inner():
        print("before")
        result = origin()
        print("after")
        return result

    return inner


@outer
def func():
    print("i am func function")
    value = (1, 2, 3, 4)
    return value


@outer
def func1():
    print("i am func1 function")
    value = (11, 12, 13, 14)
    return value


@outer
def func2():
    print("i am func2 function")
    value = (21, 22, 23, 24)
    return value


# func = outer(func)

print(func())
print(func1())
print(func2())

# --END--
