# -*- coding: utf-8 -*-
# @CreateTime : 2024/5/26 026 15:12
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/demo3.py
# @Description : 装饰器
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

"""
python中有一种特殊语法，如果你在某一个函数上方使用了

@函数名
def func():
    pass
    
在内部，会自动执行 函数名(func)，再将结果赋值给func 
相当于执行了：func = 函数名(func)
"""


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


# func = outer(func)
res = func()
print(res)

# --END--
