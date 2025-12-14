# -*- coding: utf-8 -*-
# @CreateTime : 2024/3/27 027 12:57
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : ticketProject/judge_new_user.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

import os


def is_new_user(user_name: str, folder_path: str):
    """
    判断一个用户是否已经存在。
    Args:
        user_name (str): 用户名
        folder_path (): 文件夹路径

    Returns:

    """
    file_path = os.path.join(folder_path, user_name + ".txt")
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as fp:
            fp.write(user_name + "\n")
        return True
    return False

# --END--
