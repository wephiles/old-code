# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/2/13 17:46:07
# @Project: Pycharm_Project_Set
# @File : matting.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

# site can use: https://www.remove.bg/zh/ | https://www.gaoding.com/koutu | https://www.chuangkit.com/koutu


# Third party Library: removebg site: https://www.remove.bg/api#remove-background
# # 导入库
# from removebg import RemoveBg
# api_keys = "上面获取到的key值"
# rmbg = RemoveBg(api_key, "error.log")
# # rmbg.remove_background_from_img_file("图片路径")
# rmbg.remove_background_from_img_file("xx.jpg")

import os
os.system('backgroundremover -i "cg.jpg" -o "cg_output.jpg"')

