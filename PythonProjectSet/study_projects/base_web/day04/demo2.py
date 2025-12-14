# -*- coding: utf-8 -*-
# @CreateTime : 2024/1/29 029 22:26
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/demo2.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

list_ = []

with open("demo.txt", "rb") as fp:
    for line in fp:
        new_line = line.decode("utf-8").strip()
        # if new_line:
        # 和下面的if new_line != "":效果一样
        if new_line != "":
            data = new_line.split(",")[1]
            list_.append(data)
print(list_)

# END
