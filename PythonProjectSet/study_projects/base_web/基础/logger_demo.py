# -*- coding: utf-8 -*-
# @CreateTime : 2024/3/20 020 22:30
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/logger_demo.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

import datetime


def logging(data_string: str):
    """

    Args:
        data_string ():

    Returns:

    """
    ctime = datetime.datetime.now().strftime("%Y %m %d %H %M")
    file_name = ctime + ".txt"
    with open(file_name, "a", encoding="utf-8") as fp:
        fp.write(data_string + "\n")


def run():
    while True:
        print("输入一些内容:")
        data_string = input("在下面输入内容, 输入Q/q退出程序:\n>>> ")
        if data_string.upper() == "Q":
            break
        logging(data_string)


run()

# --END--
