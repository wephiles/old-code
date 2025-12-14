# -*- coding: utf-8 -*-
# @CreateTime : 2024/1/30 030 19:30
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/demo3.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles


def sign_up():
    """注册函数

    :return: None
    """
    user_name = input("请输入用户名：")
    password = input("请输入密码：")
    with open("user_info.txt", "a", encoding="utf-8") as fp:
        fp.write(f"{1} {1}\n".format(user_name, password))


def login():
    """登录函数

    :return: None
    """
    user_name = input("请输入用户名：")
    password = input("请输入密码：")
    with open("user_info.txt", "r", encoding="utf-8") as fp:
        for line in fp:
            user_info = line.strip().split(" ")
            if user_info[0] == user_name and user_info[1] == password:
                print("登录成功！")
                break
        else:
            print("用户名或密码错误！")


def main():
    sign_up()
    login()


if __name__ == '__main__':
    main()

# END
