# -*- coding = utf-8 -*-
# @CreateTime : 2022/4/10 19:41
# @Author : 20866
# @Project: Pycharm_Project_Set
# @File : pygame 1.0.py
# @Software : PyCharm
# @InterpreterLocation : !C:\Windows.old\Users\20866\AppData\Local\Programs\Python\Python310\python.exe
# @Site : https://gitee.com/qiongjulingjun

import pygame
import sys

# 背景颜色
bg_color_1 = (0, 128, 128)
bg_color_2 = (60, 60, 60)
bg_color_3 = (255, 0, 0)

pygame.init()  # 初始化 pygame

# 主窗口
game_screen = pygame.display.set_mode((800, 600))  # 显示窗口 闪烁一下就没了
screen_rect = game_screen.get_rect()  # 显示屏幕图像的位置和形状

# 标题栏
pygame.display.set_caption('飞机大战')  # 给窗口取名字

# 飞船
ship_image = pygame.image.load(r'D:\python_3_10\game development\game_1\image\shipOK.png')  # 加载图片
ship_rect = ship_image.get_rect()

# 子弹
bullet_rect = pygame.Rect(0, 0, 20, 50)  # 四个参数分别是 位置 和 长宽

# TODO(2086689759@qq.com): 这个地方需要修改，语句似乎没有成功执行(2022/4/10)
bullet_rect.midbottom = ship_rect.midtop

# 我们让飞船的rectangle 中心点等于主窗口的 rectangle 中心点  飞船图像就会到窗口的物理中心中去
ship_rect.center = screen_rect.center

# 绘制图像
# game_screen.blit(ship_image, (0, 0))  # 把小飞机放到（0， 0）的位置上
# game_screen.blit(ship_image, (400, 300))  # 把小飞机放到（400， 300）的位置上，并不是在屏幕的物理中心
game_screen.fill(bg_color_1)  # 给屏幕上色
game_screen.blit(ship_image, ship_rect)  # 把小飞机放到获得的 ship_rect 位置上，默认0， 0
pygame.draw.rect(game_screen, bg_color_2, bullet_rect)  # 画子弹 参数： 在哪画 哪种颜色画 画什么
pygame.display.flip()  # 刷新屏幕

# 让窗口一直在，等待用户输入，便于程序进行相应的操作
while True:
    # 一直捕获键盘鼠标操作
    for event in pygame.event.get():
        # 如果点击关闭按钮，那么退出这个程序 退出值为0
        if event.type == pygame.QUIT:
            sys.exit()

# END
