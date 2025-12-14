# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/23 18:55:42
# @Project: Pycharm_Project_Set
# @File : numpy_matplotlib.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

import numpy as np
import matplotlib.pyplot as plt
# from pylab import *


if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # # subplot() 函数允许你在同一图中绘制不同的东西。
    # x = np.arange(0, 3 * np.pi, 0.1)
    # y_sin = np.sin(x)
    # y_cos = np.cos(x)
    # # 建立 subplot 网格，高为 2，宽为 1
    # # 激活第一个 subplot
    # plt.subplot(2, 1, 1)
    #
    # # 绘制第一个图像
    # plt.title('y = sin x 图像')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.plot(x, y_sin)
    #
    # # 激活第二个 subplot
    # plt.subplot(2, 1, 2)
    # # 如果这里写 2 1 1 那么两张图像重叠，一张坐标图显示两个图像
    # plt.title('y = cos x 图像')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.plot(x, y_cos)
    #
    # plt.show()

    # 条形图：
    # x = [5, 8, 10]
    # y = [12, 16, 6]
    # x_1 = [6, 9, 11]
    # y_1 = [6, 15, 7]
    #
    # plt.bar(x, y, color='r')
    # plt.bar(x_1, y_1, color='y')
    # plt.show()

    # numpy.histogram() 函数是数据的频率分布的图形表示。 水平尺寸相等的矩形对应于类间隔，称为 bin，变量 height 对应于频率。
    #
    # numpy.histogram()函数将输入数组和 bin 作为两个参数。 bin 数组中的连续元素用作每个 bin 的边界。
    # a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
    # plt.hist(a, bins=[0, 20, 40, 60, 80, 100])
    # plt.show()

    # Matplotlib 可以将直方图的数字表示转换为图形。 pyplot 子模块的 plt() 函数将包含数据和 bin 数组的数组作为参数，并转换为直方图。
    # x = np.array([1, 2, 3, 4])
    # y = np.array([3, 6, 1, 8])
    # plt.plot(x, y, 'o')
    # plt.show()

    # 两个图像画一个画布里面
    x = np.arange(0, 4*np.pi, 0.1)
    y_1 = np.sin(x)
    y_2 = np.cos(x)
    plt.plot(x, y_1, x, y_2)
    plt.show()
    pass
