# -*- coding: utf-8 -*-
# @CreateTime : 2024/3/20 020 21:36
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/demo_datetime.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles


import datetime
import hashlib

SALT = "dsawiofhdjuewhfehwqjfgudsjhuifhqew9fhuihdersgf7"


def register():
    """

    Returns:
        0
    """
    while True:
        print("Register! Input Q/q in the name statement to quit.")
        user_name = input("your name:\n>>> ")
        if user_name.upper() == 'Q':
            break
        user_pwd = input("your password:\n>>> ")

        obj_md5 = hashlib.md5(SALT.encode("utf-8"))
        obj_md5.update(user_pwd.encode("utf-8"))
        res = obj_md5.hexdigest()

        datetime_string = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(r"./db.txt", 'a', encoding='utf-8') as fp:
            line = f"{user_name} {res} {datetime_string}\n"
            fp.write(line)
    return 0


def main():
    """

    Returns:
        None
    """
    register()


if __name__ == '__main__':
    main()

# END
