# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/19 20:11:56
# @Project: Pycharm_Project_Set
# @File : data_visualization_01.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

import matplotlib.pyplot as plt  # 最基础的一个库
import numpy as np
# import plotly.express as px
# import os
# import pandas as pd


if __name__ == '__main__':
    # %matplotlib inline
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # 画折现
    # x = [1, 2, 3, 4, 5]
    # y = [1, 4, 9, 16, 25]
    # # plt.plot(x, y)
    # plt.plot(x, y, linewidth=1)  # linewidth 设置线条宽度
    # plt.title('这是一个莫得感情的折线图！！！', fontsize=10)
    # plt.xlabel('x', fontsize=10)
    # plt.ylabel('y', fontsize=10)
    # plt.show()

    # 画曲线 一元二次曲线
    # x = range(-100, 100)
    # y = [i**2 for i in x]  # y = x ** 2
    # plt.plot(x, y)
    # plt.title('这是一个莫得感情的折线图！！！', fontsize=12)
    # plt.xlabel('x', fontsize=15)
    # plt.ylabel('y', fontsize=15)
    # plt.savefig(r'../data_files/visualization_01.png')
    # plt.show()

    # 绘制一个正弦曲线
    x = np.linspace(0, 100, 1000)
    y = np.sin(x) + np.cos(x)
    plt.plot(x, y)
    plt.title('这是一个莫得感情的正弦曲线图！！！', fontsize=12)
    plt.xlabel('x', fontsize=15)
    plt.ylabel('y', fontsize=15)
    plt.show()
    pass
