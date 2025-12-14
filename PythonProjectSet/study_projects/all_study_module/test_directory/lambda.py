# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/21 12:21:55
# @Project: Pycharm_Project_Set
# @File : lambda.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

import json


# def make(n):
#     # Learn lambda. 学习lambda表达式。
#     #
#     # 关键字用于创建小巧的匿名函数。lambda a, b: a+b 函数返回两个参数的和。
#     # Lambda 函数可用于任何需要函数对象的地方。在语法上，匿名函数只能是单个
#     # 表达式。在语义上，它只是常规函数定义的语法糖。与嵌套函数定义一样，
#     # lambda 函数可以引用包含作用域中的变量：
#
#     return lambda x: x+n
#
#
# def a_function(a: int, b: str = 'hello') -> None:
#     """This is a function which test document notes
#
#     Okay, this function is just for testing.
#     """
#     print(a, b)


# f = make(10)
#
# print(f)
#
# print(f(5))
# print(f(4))

# print(a_function.__doc__)
# print(a_function(1, '???'))
# end of file


def main() -> str:
    text = ' '
    # with open('test_text.txt', 'a+', encoding='utf-8') as fp:
    #     # 以列表形式读取文件所有行
    #     text_ = fp.readlines()
    #     values = ('hello', 520)
    #     string = str(values)
    #     fp.write(string)
    # # print(fp.closed)
    # print(text_)
    x = [1, 'hello', 36.5]
    y = json.dumps(x)
    print(y)
    values = [1, 'hello', 36.5]
    # dump 只序列化 text file
    with open('text.txt', 'w', encoding='utf-8') as fp:
        fp.write(str(values))
        json.dump(x, fp)
    with open('text.txt', 'r', encoding='utf-8') as f:
        text_ = f.read()
        print(text_)
    pass
    return text


if __name__ == '__main__':
    # for x in range(1, 11):
    #     print('{:2d} {:3d} {:4d}'.format(x, x * x, x * x * x))
    main()
