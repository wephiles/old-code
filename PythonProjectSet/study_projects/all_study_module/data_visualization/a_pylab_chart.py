# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/26 11:42:03
# @Project: Pycharm_Project_Set
# @File : a_pylab_chart.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

from pylab import *


def main():
    # n = 256
    # x = np.linspace(-np.pi, np.pi, n)
    # y = np.sin(2*x)
    #
    # plt.axes([0.025, 0.025, 0.95, 0.95])
    # plot(x, y + 1, color='blue', alpha=1.00)
    # fill_between(x, 1, y + 1, color='blue', alpha=.15)
    #
    # plot(x, y - 1, color='blue', alpha=1.00)
    # plt.fill_between(x, -1, y - 1, (y - 1) > -1, color='blue', alpha=.25)
    # plt.fill_between(x, -1, y - 1, (y - 1) < -1, color='red', alpha=.25)
    # show()

    # 随机点
    # n = 1024
    # x = np.random.normal(0, 1, n)
    # y = np.random.normal(0, 1, n)
    # scatter(x, y)
    # show()

    # 条形图
    n = 12
    x = np.arange(n)
    y_1 = (1 - x / float(n)) * np.random.uniform(0.5, 1, n)
    y_2 = (1 - x / float(n)) * np.random.uniform(0.5, 1, n)
    bar(x, +y_1, facecolor='yellow', edgecolor='white')
    bar(x, -y_2, facecolor='blue', edgecolor='white')

    for a, b in zip(x, y_1):
        text(a+0.4, b+0.05, '%.2f' % b, ha='center', va='bottom')
        ylim(-1.25, 1.25)
    # for c, d in zip(x, y_2):
    #     text(c+0.4, d+0.05, '%.2f' % d, ha='center', va='bottom')
    #     ylim(-1.25, 1.25)
    pass


if __name__ == '__main__':
    main()
