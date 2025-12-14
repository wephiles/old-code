# -*- coding: utf-8 -*-
# @CreateTime : 2024/2/26 026 17:27
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/random_demo.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

# 夹带私货 让某个工号容易出现

import random

# 1. 创建三百名员工
user_list = [f"工号-{i}" for i in range(1, 301)]

# 2. 奖项信息
data_list = [
    ("三等奖", 5),
    ("二等奖", 3),
    ("一等奖", 2),
    ("特等奖", 1)
]

# 3. 抽奖
for item in data_list:
    text = item[0]
    count = item[1]
    if text == "特等奖":
        print("谁谁谁中奖")
        break
    prize_list = random.sample(user_list, count)  # 抽什么奖 以多少个
    for name in prize_list:
        user_list.remove(name)
    print(text, prize_list)
    input("点击回车继续。")


# --END--
