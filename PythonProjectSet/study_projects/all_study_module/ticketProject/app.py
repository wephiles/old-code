# -*- coding: utf-8 -*-
# @CreateTime : 2024/3/24 024 22:14
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : ticketProject/app.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

import os
from monitor import monitor, judge_new_user
from monitor.history import history
from monitor.booking import booking


def run():
    """

    Returns:

    """
    # 监测是否存在文件夹
    folder_path = os.path.join("db", "files")
    monitor.monitoring(folder_path)

    # 判断是不是新用户
    user_name = input("Please enter your username:\n>>> ")
    if judge_new_user.is_new_user(user_name, folder_path):
        print("New User!")
    else:
        print("Old User!")
    file_path = os.path.join(folder_path, user_name + ".txt")

    # 功能选择
    func_dict = {
        "1": history,
        "2": booking
    }
    while True:
        print("1: 查询历史订单  2: 订票 Q/q: 退出")
        choice = input("请选择功能(输入q/Q退出)、\n>>> ")
        if choice.lower() == "q":
            break
        func_ = func_dict.get(choice)
        if not func_:
            print("请输入正确的选项！")
            continue
        func_(file_path)


run()

# --END--
