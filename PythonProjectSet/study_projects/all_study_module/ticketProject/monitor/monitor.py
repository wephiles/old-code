# -*- coding: utf-8 -*-
# @CreateTime : 2024/3/24 024 22:24
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : ticketProject/monitor.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles


import os


def monitoring(db_folder=None):
    """监测，如果有指定的目录，那么啥事也不干，否则新建没有的目录。

    Returns:
        None
    """
    if not os.path.exists(db_folder):
        os.makedirs(db_folder)

# --END--
