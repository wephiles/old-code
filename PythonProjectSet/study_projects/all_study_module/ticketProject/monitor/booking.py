# -*- coding: utf-8 -*-
# @CreateTime : 2024/3/27 027 13:21
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : ticketProject/booking.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

from datetime import datetime


def booking(user_file_path):
    """
    订票系统
    Args:
        user_file_path ():

    Returns:

    """
    location = input("请输入景区名称！")
    count = input("请输入购票数量！")
    ctime = datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")
    line = "{},{},{}\n".format(location, count, ctime)
    with open(user_file_path, "a+", encoding="utf-8") as fp:
        fp.write(line)

# --END--
