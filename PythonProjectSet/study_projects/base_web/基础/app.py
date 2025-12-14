# -*- coding: utf-8 -*-
# @CreateTime : 2024/2/26 026 10:05
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/app.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

# import utils
#
# choice = input("输入序号: \n>>> ")
# print(utils.str_to_int(choice))

# import hashlib
#
# data = "admin"
# obj = hashlib.md5()
# obj.update(data.encode("utf-8"))
# res = obj.hexdigest()
# print(res)

# import hashlib
#
# DB_FILE_PATH = "db.txt"
# SALT = "fjiwojefioejwfojewoiprfjewrj"
#
#
# def md5(data_string):  # 加密字符串
#     obj = hashlib.md5(SALT.encode("utf-8"))
#     obj.update(data_string.encode("utf-8"))
#     res = obj.hexdigest()
#     return res
#
#
# def login():
#     print("用户登录!")
#     user_name = input("输入用户名\n>>> ")
#     pwd = input("输入密码\n>>> ")
#     encrypted_pwd = md5(pwd)
#     is_successful = False
#
#     # 逐行对比
#     with open(DB_FILE_PATH, "r", encoding="utf-8") as fp:
#         for line in fp:
#             data_list = line.strip().split(" ")
#             if data_list[0] == user_name and encrypted_pwd == data_list[1]:
#                 is_successful = True
#     if is_successful is True:
#         print("登录成功!")
#     else:
#         print("登录失败!")
#
#
# def register():
#     print("注册")
#     user_name = input("用户名 >>> ")
#     password = input("密码 >>> ")
#     encrypt_pwd = md5(password)  # 加密密码
#     line = "{} {}\n".format(user_name, encrypt_pwd)
#     with open(DB_FILE_PATH, "a", encoding="utf-8") as fp:
#         fp.write(line)
#
#
# def run():
#     func_dict = {
#         "1": register,
#         "2": login
#     }
#     choice = input("选择序号: 1 注册	2 登录 \n>>> ")
#     func = func_dict.get(choice)
#     if not func:
#         print("序号错误")
#         return
#     func()
#
#
# run()

def run():
    """

    Returns:

    """


run()

# --END--
