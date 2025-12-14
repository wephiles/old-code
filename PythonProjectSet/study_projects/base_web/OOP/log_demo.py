# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/28 028 20:39
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/log_demo.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

import logging
import traceback

logging.basicConfig(
    filename="log.log",
    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
    # asctime 什么时候出的错
    # name 模块名
    datefmt="%Y-%m-%d %H:%M:%S %p",
    level=10  # 日志级别 大于等于的时候10
)


# logging.debug("debug")  # 测试时候的日志
# logging.info("info")  # 正常的信息
# logging.warning("warning")  # 警告 能用
# logging.error("error")  # 报错
# logging.critical("critical")  # 非常严重错误
# logging.log(10, "loggg")


def func():
    try:
        a = a + 1
    except Exception as e:
        # 获取当前错误的堆栈信息
        msg = traceback.format_exc()
        logging.error(msg)


func()

# --END--
