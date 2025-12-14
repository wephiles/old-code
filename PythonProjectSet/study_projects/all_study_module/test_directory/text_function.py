# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/20 23:29:39
# @Project: Pycharm_Project_Set
# @File : text_function.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun


# def function(arg=0) -> int:
#     return arg
#
#
# def function_pos_only(arg_1=5, arg_2=3, /) -> int:
#     return arg_1*10 + arg_2


# def function_only_kwd(*, arg_1=0, arg_2=0) -> int:
#     return arg_1*10 + arg_2
#     pass


# def a_function(a=0, b=0, c=0, d=0, e=0,  *arguments, **keywords) -> int:
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(e)
#     for x in arguments:
#         print(x)
#     for kw in keywords:
#         print(str(kw), ': ', str(keywords[kw]))
#     return 1


# def another_function(a=0, b=0, c=0, *arguments, **keywords) -> int :
#     """
#     测试一哈函数哈！
#     """
#     print(a, b, c)
#     for item in arguments:
#         print(item)
#     for kw in keywords:
#         print(keywords[kw])
#     return 1


# def function_common(a, b, c, **name) -> int :
#     print(a, b, c)
#     for item in name:
#         print(name[item])
#     return 1


if __name__ == '__main__':
    # print(function(arg=1))  # 1
    # print(function(5))  # 5
    #
    # print(function_pos_only(1, 2))  # 12
    # print(function_pos_only(arg_1=1, arg_2=2))
    # 只能传位置参数
    #  function_pos_only() got some positional-only
    #  arguments passed as keyword arguments: 'arg_1, arg_2'
    # print(function_only_kwd(1, 2))  # TypeError: function_only_kwd() takes 0 positional arguments but 2 were given
    # print(function_only_kwd(arg_1=1, arg_2=2))  # 12
    # a_function(1, 2, c=3, d=4, e=5, name='hello', age=18)
    # another_function(1, 2, 3, 'hello', 'world', hello='hello', world='world')
    # function_common(a=1, b=2, c=3, he='hello', she='world')
    for i in range(0, 10):
        print(i)
    pass
