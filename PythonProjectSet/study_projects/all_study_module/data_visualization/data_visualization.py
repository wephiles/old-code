# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/18 19:49:29
# @Project: Pycharm_Project_Set
# @File : data_visualization.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

import matplotlib.pyplot as plt  # 最基础的一个库
import numpy as np
# import plotly.express as px
import os
import pandas as pd
# 绘图基础


if __name__ == '__main__':
    # %matplotlib inline
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # x = np.linspace(0, 100, 1000)
    # y = np.sin(x)
    # plt.plot(x, y, c='red', lw=2, ls='-')
    # # plt.show()
    # # print('Begin now!!! ')
    # plt.plot(x, y, ls='-', marker='|', markersize=5, c='black', markeredgecolor='blue', markerfacecolor='black')
    # plt.title('x 和 y 关系')
    # plt.legend(loc='upper center')
    # plt.show()

    # x = np.linspace(0, 10, 100)
    # y = np.sin(x)
    # plt.plot(x, y, ls='-', lw=2, label='x和y的关系 y = sin x')
    # plt.legend(loc='upper center')  # 图例
    # plt.show()
    # x = np.arange(0, 1.1, 0.01)
    # y = x ** 2
    # plt.figure(figsize=(4, 4), dpi=100, facecolor='white')
    # # dpi是分辨率 facecolor是边框颜色 figsize是大小
    # plt.title('这是一幅图')
    # plt.xlabel('x1')  # x轴标签
    # plt.ylabel('y')
    # plt.xlim(0, 1)
    # plt.ylim(0, 1)
    # plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1])  # x的刻度
    # plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])  # y的刻度
    # plt.plot(x, y, label='y = x ^ 2')
    # # plt.legend(loc='upper center')
    # plt.legend(loc='best')

    # 图片的保存
    # plt.savefig(r'D:\系统默认\桌面\可视化.jpg')
    # plt.savefig(r'D:\系统默认\桌面\可视化.png')
    # plt.savefig(r'D:\系统默认\桌面\可视化.pdf')
    # plt.show()
    # 简单图形绘制: 饼图 条形图 直方图 散点图
    # 饼图
    os.chdir(r'../data_files')  # 改变当前工作目录
    # data = pd.read_excel('text_1.xlsx')  # 读取我们的Excel表格
    # # print(data)
    # # data.head(2)  # 打印前两行数据
    # data_1 = data.groupby('diqu').mean()['xiaoliang']  # 分组并且汇总求和
    # # print(data_1)
    # # print(data_1.index)
    # x_data = data_1.values
    # y_data = data_1.index

    # 下面绘制饼图
    # explode = [0, 0.1, 0, 0, 0, 0.1]  # 饼图的大小和形状 数据越大，突出显示越大
    # colors = ['red', 'blue', 'yellow', 'green', 'pink', 'purple']
    # plt.pie(x=x_data, explode=explode, labels=y_data, colors=colors, autopct='%.1f%%',
    #         pctdistance=0.7, labeldistance=1.1, startangle=120,
    #         radius=1.2, counterclock=False, wedgeprops={'linewidth': 1.5, 'edgecolor': 'green'},
    #         textprops={'fontsize': 10, 'color': 'black'})
    # plt.title('这是一张莫得感情的饼图！', pad=30)
    # plt.savefig(r'../data_files/visualization.jpg')
    # plt.show()

    # 下面绘制条形图
    # plt.bar(x=range(0, len(x_data)), height=x_data,
    #         align='center', color='y', tick_label=y_data)
    # plt.xlabel('x', labelpad=20)  #
    # plt.ylabel('y', labelpad=20)
    # plt.title(' x 和 y 的关系 ')
    # plt.show()

    # 下面绘制直方图
    # plt.hist(x=data['xiaoliang'], bins=20, color='r', edgecolor='black',
    #          density=False)  # denisty表示是否以频数的形式展示
    # plt.title('这是一个莫得感情的直方图')
    # plt.show()

    # 下面绘制散点图
    data = pd.read_excel('text_1.xlsx')
    print(data.head(2))
    plt.scatter(x=data['jiage'], y=data['xiaoliang'], color='steelblue', marker='o', s=10)
    plt.xlabel('价格')
    plt.ylabel('销量')
    plt.title('这是一个莫得感情的散点图')
    plt.show()
    pass
