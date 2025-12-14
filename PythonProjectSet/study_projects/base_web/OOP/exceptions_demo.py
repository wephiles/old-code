# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/28 028 18:56
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/exceptions_demo.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles


# import os
#
#
# class FileExistException(Exception):
#     pass
#
#
# class KeyInvalidError(Exception):
#     pass
#
# def func(path, prev):
#     """
#     去path路径的文件中找前缀为prev的数据，并返回
#         1000 成功
#         1001 文件不存在
#         1002 关键字为空
#         1003 未知错误
#         ...
#     Args:
#         path ():
#         prev ():
#
#     Returns:
#
#     """
#     response = {"code": 1000, "data": None}
#
#     try:
#         if not os.path.exists(path):
#             response["code"] = 1001
#             response["data"] = "文件不存在"
#             return response
#         if not prev:
#             response["code"] = 1002
#             response["data"] = "关键字为空"
#             return response
#         pass
#     except Exception as e:
#         response["code"] = 1003
#         response["data"] = "未知错误"
#     return response
#
#
# def new_func(path, prev):
#     """
#     去path路径的文件中找前缀为prev的数据，并返回
#         1000 成功
#         1001 文件不存在
#         1002 关键字为空
#         1003 未知错误
#         ...
#     Args:
#         path ():
#         prev ():
#
#     Returns:
#
#     """
#     response = {"code": 1000, "data": None}
#
#     try:
#         if not os.path.exists(path):
#             raise FileExistException()
#         if not prev:
#             raise KeyInvalidError()
#         pass
#
#     except FileExistException as e:
#         response["code"] = 1001
#         response["data"] = "文件不存在"
#     except KeyInvalidError as e:
#         response["code"] = 1002
#         response["data"] = "关键字为空"
#     except Exception as e:
#         response["code"] = 1003
#         response["data"] = "未知错误"
#     return response
#
#
# def show():
#     return 8
#
#
# def run():
#     v1 = func()
#     v2 = show()

class MyException(Exception):
    """
    自定义异常类。
    """
    def __init__(self, code, message):
        self.code = code
        self.message = message


try:
    raise MyException(1000, "自定义异常啦")
except MyException as e:  # 捕获异常 这个e是一个对象
    print(e.code, e.message)
except Exception as e:  # 捕获异常 这个e是一个对象
    print(e)

# --END--
