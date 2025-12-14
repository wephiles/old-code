# -*- coding: utf-8 -*-
# @CreateTime : 2024/5/26 026 14:58
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/demo2.py
# @Description : 装饰器
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

def func():
    print("i am func function")
    value = (1, 2, 3, 4)
    return value


def outer(origin):
    def inner():
        print("before")
        result = origin()
        print("after")
        return result
    return inner


func = outer(func)
res = func()
print(res)

# --END--
