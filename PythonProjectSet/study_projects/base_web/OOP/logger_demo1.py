# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/28 028 21:07
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/logger_demo1.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# import logging
# import traceback
#
# logging.basicConfig(
#     filename="log1.log",
#     format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
#     # asctime 什么时候出的错
#     # name 模块名
#     datefmt="%Y-%m-%d %H:%M:%S %p",
#     level=10  # 日志级别 大于等于的时候10
# )
#
# logging.error("loging 1")
#
# logging.basicConfig(
#     filename="log2.log",
#     format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
#     # asctime 什么时候出的错
#     # name 模块名
#     datefmt="%Y-%m-%d %H:%M:%S %p",
#     level=10  # 日志级别 大于等于的时候10
# )
# logging.error("loging 2")


import logging

file_handler_obj = logging.FileHandler("log1.log", 'a', encoding='utf-8')
fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s")
file_handler_obj.setFormatter(fmt)

logger1 = logging.Logger("s1", level=logging.ERROR)
logger1.addHandler(file_handler_obj)
logger1.error("logger1 error")

file_handler_obj = logging.FileHandler("log2.log", 'a', encoding='utf-8')
fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s")
file_handler_obj.setFormatter(fmt)

logger2 = logging.Logger("s1", level=logging.WARNING)
logger2.addHandler(file_handler_obj)
logger2.warning("logger2 warning")

# --END--
