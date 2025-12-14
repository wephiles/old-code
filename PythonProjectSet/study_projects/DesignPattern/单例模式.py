#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2025/01/05 21:26
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: DesignPattern
# @FileName   : DesignPattern/单例模式.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# from abc import ABCMeta, abstractmethod
pass

# ########################## 自己写的 ##########################
pass
# import random
# 
# show_dict = {
#     1: 'C',
#     2: 'D',
#     3: 'E',
#     4: 'F',
#     5: 'G',
#     6: 'A',
#     7: 'B',
#     'i': 'C',
# }
# 
# list_music = [1, 2, 3, 4, 6, 5, 7, 'i']
# 
# while True:
#     x = random.choice(list_music)
#     print(x, show_dict[x], end='')
#     print("\033[H\033[J", end="")
#     input()
pass

# ########################## deepseek ##########################
pass
# import random
# import sys
#
# show_dict = {
#     1: 'C',
#     2: 'D',
#     3: 'E',
#     4: 'F',
#     5: 'G',
#     6: 'A',
#     7: 'B',
#     'i': 'C',
# }
#
# list_music = [1, 2, 3, 4, 6, 5, 7, 'i']
#
# while True:
#     x = random.choice(list_music)
#     sys.stdout.write(f"\r\x1b[2K{x} {show_dict[x]}")
#     sys.stdout.flush()
#     input()
#     sys.stdout.write("\r\x1b[2K")
#     sys.stdout.flush()

# --END--
pass

# ########################## 紫东太初 ##########################
pass
# import random
# import os
#
# show_dict = {
#     1: 'C',
#     2: 'D',
#     3: 'E',
#     4: 'F',
#     5: 'G',
#     6: 'A',
#     7: 'B',
#     'i': 'C',
# }
#
# list_music = [1, 2, 3, 4, 6, 5, 7, 'i']
#
#
# # 用于清屏的函数
# def clear_screen():
#     # 对于Windows系统使用'cls'，对于Unix/Linux/Mac系统使用'clear'
#     os.system('cls' if os.name == 'nt' else 'clear')
#
#
# while True:
#     x = random.choice(list_music)
#     # 在每次迭代开始时先清空屏幕
#     clear_screen()
#     # 打印音符而不换行
#     print(x, show_dict[x], end='')
#     # 等待用户按下回车键
#     input()

# ########################## 智谱清言 ##########################
pass
# import random
# import os
# import sys
#
# show_dict = {
#     1: 'C',
#     2: 'D',
#     3: 'E',
#     4: 'F',
#     5: 'G',
#     6: 'A',
#     7: 'B',
#     'i': 'C',
# }
#
# list_music = [1, 2, 3, 4, 6, 5, 7, 'i']
#
#
# def clear_screen():
#     # 根据操作系统执行清屏命令
#     os.system('cls' if os.name == 'nt' else 'clear')
#
#
# while True:
#     x = random.choice(list_music)
#     print(x, show_dict[x], end='')
#     input()  # 等待用户输入回车
#     clear_screen()  # 清除屏幕
pass

# ########################## KIMI ##########################
pass
# import random
# import os
#
# show_dict = {
#     1: 'C',
#     2: 'D',
#     3: 'E',
#     4: 'F',
#     5: 'G',
#     6: 'A',
#     7: 'B',
#     'i': 'C',
# }
#
# list_music = [1, 2, 3, 4, 6, 5, 7, 'i']
#
# while True:
#     x = random.choice(list_music)
#     print(x, show_dict[x])
#     input()
#     os.system('cls' if os.name == 'nt' else 'clear')
pass

# ########################## 海螺 ##########################
pass
# import random
# import sys
# import time
#
# show_dict = {
#     1: 'C',
#     2: 'D',
#     3: 'E',
#     4: 'F',
#     5: 'G',
#     6: 'A',
#     7: 'B',
#     'i': 'C',
# }
#
# list_music = [1, 2, 3, 4, 6, 5, 7, 'i']
#
#
# def clear_line():
#     # ANSI 转义序列用于清除当前行
#     sys.stdout.write('\033[2K\033[1G')
#     sys.stdout.flush()
#
#
# while True:
#     x = random.choice(list_music)
#     print(f"{x} {show_dict[x]}", end='', flush=True)
#     input()  # 等待用户按回车
#     clear_line()  # 清除当前行
pass
# import random
# import os
# import sys
# import time
#
# show_dict = {
#     1: 'C',
#     2: 'D',
#     3: 'E',
#     4: 'F',
#     5: 'G',
#     6: 'A',
#     7: 'B',
#     'i': 'C',
# }
#
# list_music = [1, 2, 3, 4, 6, 5, 7, 'i']
#
#
# def clear_screen():
#     # 根据操作系统选择清屏命令
#     if os.name == 'nt':
#         os.system('cls')
#     else:
#         os.system('clear')
#
#
# while True:
#     x = random.choice(list_music)
#     print(f"{x} {show_dict[x]}", end='', flush=True)
#     input()  # 等待用户按回车
#     clear_screen()  # 清屏
pass

# ########################## 讯飞星火 ##########################
pass
# import random
# import os
#
# show_dict = {
#     1: 'C',
#     2: 'D',
#     3: 'E',
#     4: 'F',
#     5: 'G',
#     6: 'A',
#     7: 'B',
#     'i': 'C',
# }
#
# list_music = [1, 2, 3, 4, 6, 5, 7, 'i']
#
# while True:
#     x = random.choice(list_music)
#     # Clear the screen (works for both Windows and Unix-based systems)
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print(x, show_dict[x], end='')
#     input()
pass

# ########################## 文心一言 ##########################
pass
# import random
# import os
# import sys
#
# # ANSI转义序列
# CLEAR_LINE = '\033[K'  # 清空当前行从光标位置到行尾的内容
# MOVE_UP = '\033[F'  # 将光标上移一行
# MOVE_TO_START = '\033[H'  # 将光标移动到屏幕左上角（如果需要完全清空屏幕）
#
# show_dict = {
#     1: 'C',
#     2: 'D',
#     3: 'E',
#     4: 'F',
#     5: 'G',
#     6: 'A',
#     7: 'B',
#     'i': 'C (high)',  # 为了区分八度，可以稍微修改显示
# }
#
# list_music = [1, 2, 3, 4, 6, 5, 7, 'i']
#
# try:
#     while True:
#         # 清空当前行并移动到行首（如果需要完全清空屏幕，可以使用 MOVE_TO_START + CLEAR_SCREEN）
#         sys.stdout.write(CLEAR_LINE + MOVE_UP)
#         sys.stdout.flush()
#
#         x = random.choice(list_music)
#         # 打印新的数据，但不换行
#         sys.stdout.write(f"{x} {show_dict[x]}")
#         sys.stdout.flush()
#
#         input()  # 等待用户输入
# except KeyboardInterrupt:
#     print("\n程序已退出。")
pass

# ########################## 通义千问 ##########################
pass
# import random
# import os
# import platform
#
# # 根据操作系统选择清屏命令
# CLEAR_COMMAND = 'cls' if platform.system() == 'Windows' else 'clear'
#
# show_dict = {
#     1: 'C',
#     2: 'D',
#     3: 'E',
#     4: 'F',
#     5: 'G',
#     6: 'A',
#     7: 'B',
#     'i': 'C',
# }
#
# list_music = [1, 2, 3, 4, 6, 5, 7, 'i']
#
# while True:
#     # 在每次循环开始时清屏
#     os.system(CLEAR_COMMAND)
#
#     x = random.choice(list_music)
#     print(x, show_dict[x], end='')
#
#     # 等待用户输入回车后继续
#     input()
pass

# ########################## 腾讯元宝 ##########################
pass
# import random
# import os
# import platform
#
# # 定义显示字典
# show_dict = {
#     1: 'C',
#     2: 'D',
#     3: 'E',
#     4: 'F',
#     5: 'G',
#     6: 'A',
#     7: 'B',
#     'i': 'C',
# }
#
# # 定义音阶列表
# list_music = [1, 2, 3, 4, 6, 5, 7, 'i']
#
#
# def clear_screen():
#     """
#     根据操作系统类型清屏。
#     """
#     if platform.system().lower() == "windows":
#         os.system('cls')  # Windows 系统使用 cls 命令
#     else:
#         os.system('clear')  # Unix/Linux/Mac 系统使用 clear 命令
#
#
# while True:
#     x = random.choice(list_music)
#     os.system('clear' if platform.system().lower() != 'windows' else 'cls')  # 清屏
#     print(f"{x} {show_dict[x]}")  # 打印当前音阶
#     input("")  # 等待用户按下回车键

# ########################## GPT ##########################

import random

show_dict = {
    1: 'C',
    2: 'D',
    3: 'E',
    4: 'F',
    5: 'G',
    6: 'A',
    7: 'B',
    'i': 'C',
}

list_music = [1, 2, 3, 4, 6, 5, 7, 'i']

while True:
    x = random.choice(list_music)
    print(x, show_dict[x], end='')
    input()
