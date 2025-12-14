# -*- coding: utf-8 -*-
# @CreateTime : 2024/1/12 012 20:55
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/demo1.py
# @Description :
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

# for i in range(0, 10):
#     if i == 7:
#         continue
#     else:
#         print(i)

# count = 1
#
# while count < 11:
#     if count == 7:
#         count += 1
#         continue
#     else:
#         print(count)
#         count += 1

# 占位符:

# # text = '我的名字叫 {0} ,就是 {0} 的 {0},今年 {1} 岁 {0}'.format("计算机", 20)
# text = '我的名字叫{},我今年{}岁,我爱吃{}'.format("计算机", 20, 'Apple')
# print(text)

# tpl = "我的名字叫{} 今年{}岁"
# v1 = tpl.format("计算机", 19)
# print(v1)
# print(tpl)

# text = '我的名字叫{name},我今年{age}岁,我爱吃{food}'.format(name="计算机", age=20, food='Apple')
# print(text)

# text = '我的名字叫 %s ,今年 %d 岁' % ('计算机', 19)
# print(text)

# text = '我的名字叫 %s ,今年 %d 岁'
# v1 = text % ('计算机', 19)
# print(v1)

# name = "计算机"
# age = 19
# text = f'我的名字叫{name}, 我今年{age}岁'
# print(text)

# v1 = 1 and 2
# v2 = 2 and 4
# print(v1)
# print(v2)
#
# v11 = 2 and 1
# v12 = 4 and 2
# print(v11)
# print(v12)
#
# v3 = 0 and 1
# v4 = 1 and 0
# print(v3)
# print(v4)

# v1 = 1 and 8 or 9 and 10 or 11 or 12 and 0 or "" and "计算机"
# print(v1)
#
# data = 238  # 十进制
# v1 = bin(data)   # 二进制
# v2 = oct(data)   # 八进制
# v3 = hex(data)   # 十六进制
#
# print(v1, v2, v3, end=" ")
#
# print()
#
# d1 = int("0b11101110", base=2)
# d2 = int("0o356", base=8)
# d3 = int("0xee", base=16)
# print(d1, d2, d3, end=" ")

# name = "计算机"  # ->     字符串类型 在Python内部 使用unicode编码存储(ucs4)
# data = name.encode('utf-8')  # ->     字节类型  使用UTF-8编码存储
# print(name, data)

# if "999".isdecimal():
#     print('true')
# else:
#     print("false")

# while True:
#     input_string = input("请输入一个数字")
#     if input_string.isdecimal():
#         break
# print(input_string)

# name = " 计算 机 "
# n1 = name.strip()  # "计算 机"   只能去除两边的空格
# n2 = name.lstrip()  # "计算 机 "  只能去除左边的空格
# n3 = name.rstrip()  # " 计算 机"  只能去除左边的空格
# print('"', end="")
# print(n1, end='"\n')
#
# print('"', end="")
# print(n2, end='"\n')
#
# print('"', end="")
# print(n3, end='"\n')

# text = "计算机科学与技术"
# new_text = text.replace("计算机", "软件")
#
# print(text)
# print(new_text)

# # 让用户输入一段文本 如果出现 计算机，替换成***
# text = input("请输入您的评论\n>>> ")
# new_text = (text.replace("计算机", "***").replace("苍老师",
#             "***").replace("坤坤", "**"))
# print(new_text)

# file_name = "hello.py"
#
# # 如何获得扩展名
# data_list = file_name.split(".")  # 根据传进去的参数分割
# print(data_list[-1])

# data_list_new = []
# text = "计算机, root, 18, 123@qq.com"
# data_list = text.split(",")
# for item in data_list:
#     data_list_new.append(item.strip())
# print(data_list_new)

# data_list = ["计算机", "科学", "与", "技术"]
# new_data = " ".join(data_list)
# print(new_data)

# data = "哈哈"
# v1 = data.encode("utf-8")
# print(v1)

# data = "哈哈"
# v1 = data.encode("utf-8")
# v2 = v1.decode("utf-8")
# print(v1, v2)

# name = "computers"
# text = name.center(13, "*")
# print(text)

# name = "computer"
# text = name.ljust(13, "#")
# print(text)

# name = "computer"
# text = name.rjust(13, "#")
# print(text)

# name = "computer"
# v1 = name.zfill(10)
# print(v1)

# name = "cs"
# print(len(name))

text = "computer"
print(text[1])


# END
