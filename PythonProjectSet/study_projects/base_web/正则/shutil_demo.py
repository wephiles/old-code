# -*- coding: utf-8 -*-
# @CreateTime : 2024/3/30 030 20:46
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/shutil_demo.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

import os
import shutil

folder_path = r"D:\CSProjects\PycharmProjects\studyProject\wupeiqiStudyBilibili\day07\day01"

for name in os.listdir(folder_path):
    if name.rsplit(".", maxsplit=1)[-1] == "mp4":  # 参数“.”表示从右边(rsplit)分割 maxsplit=1表示分割右边第一个点
        new_name = name.replace("fullstack s7 day01 ", "")
        shutil.move(os.path.join(folder_path, name), os.path.join(folder_path, new_name))


# --END--
