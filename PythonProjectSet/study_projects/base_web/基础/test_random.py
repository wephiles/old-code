# -*- coding: utf-8 -*-
# @CreateTime : 2024/2/25 025 20:29
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/test_random.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles


import random


def main() -> int:
    # 随机获取65-90的数字 利用chr转换成字母
    char_list = []
    for i in range(6):
        num = random.randint(65, 90)  # [65, 90]之间的随机数。
        char_list.append(chr(num))
    print("".join(char_list))
    return 0


if __name__ == "__main__":
    main()

# --END--
