# -*- coding: utf-8 -*-
# @CreateTime : 2024/3/27 027 13:21
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : ticketProject/history.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

import os


def history(user_file_path):
    """

    Args:
        user_file_path ():

    Returns:

    """
    # 监测文件是否存在 如果不存在，输出 无历史记录
    if not os.path.exists(user_file_path):
        print("无历史记录！")
        return

    # 如果存在，读取文件内容 逐行打印
    print("=====历史记录=====")
    with open(user_file_path, "r", encoding="utf-8") as fp:
        for line in fp:
            line = line.strip()
            print(line, end=" ")
    print()

# --END--
