# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/24 17:51:51
# @Project: Pycharm_Project_Set
# @File : a_matplotlib_chart.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

# import numpy as np
# import matplotlib.pyplot as plt
# import numpy as np
from pylab import *


def main():
    """ 绘图标记测试

    绘图过程如果我们想要给坐标自定义一些不一样的标记，就可以使用 plot() 方法的 marker 参数来定义。
    fmt 参数定义了基本格式，如标记、线条样式和颜色。 fmt = '[marker][line][color]'
    """
    # x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # y = np.array([2, 5, 8, 7, 10, 2, 3, 5, 9])
    # # plt.plot(x, y, ',:r')  # "," 表示像素点 ":" 表示虚线 "r" 表示红色
    # plt.plot(x, y, marker='o', ms=5, color='k', linestyle='-',
    #          markerfacecolor='w', markeredgecolor='k', linewidth='2')  # ms == marksize 标记的大小
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.grid(axis='y')
    # plt.show()

    # Matplotlib 网格线
    # 我们可以使用 pyplot 中的 grid() 方法来设置图表中的网格线。
    # matplotlib.pyplot.grid(b=None, which='major', axis='both', )

    # Matplotlib 绘制多图
    # 我们可以使用 pyplot 中的 subplot() 和 subplots() 方法来绘制多个子图。
    #
    # subplot() 方法在绘图时需要指定位置，subplots() 方法可以一次生成多个，在调用时只需要调用生成对象的 ax 即可。
    #
    # subplot
    # subplot(nrows, ncols, index, **kwargs)
    # subplot(pos, **kwargs)
    # subplot(**kwargs)
    # subplot(ax)

    # 画多个图
    # x = np.array([0, 6])
    # y = np.array([0, 100])
    # plt.subplot(2, 1, 1)
    # plt.plot(x, y)
    # plt.title('x_1 and y_1')
    #
    # x_1 = np.array([0, 4])
    # y_1 = np.array([0, 10])
    # plt.subplot(2, 1, 2)
    # plt.title('x_2 and y_2')
    # plt.plot(x_1, y_1)
    #
    # plt.show()

    # # plot 1:
    # x = np.array([0, 6])
    # y = np.array([0, 100])
    #
    # plt.subplot(2, 2, 1)
    # plt.plot(x, y)
    # plt.title("plot 1")
    #
    # # plot 2:
    # x = np.array([1, 2, 3, 4])
    # y = np.array([1, 4, 9, 16])
    #
    # plt.subplot(2, 2, 2)
    # plt.plot(x, y)
    # plt.title("plot 2")
    #
    # # plot 3:
    # x = np.array([1, 2, 3, 4])
    # y = np.array([3, 5, 7, 9])
    #
    # plt.subplot(2, 2, 3)
    # plt.plot(x, y)
    # plt.title("plot 3")
    #
    # # plot 4:
    # x = np.array([1, 2, 3, 4])
    # y = np.array([4, 5, 6, 7])
    #
    # plt.subplot(2, 2, 4)
    # plt.plot(x, y)
    # plt.title("plot 4")
    #
    # plt.suptitle("RUNOOB subplot Test")
    # plt.show()

    # # 创建一些测试数据 -- 图1
    # x = np.linspace(0, 2 * np.pi, 400)
    # y = np.sin(x ** 2)
    #
    # # 创建一个画像和子图 -- 图2
    # fig, ax = plt.subplots()
    # ax.plot(x, y)
    # ax.set_title('Simple plot')
    #
    # # 创建两个子图 -- 图3
    # f, (ax1, ax2) = plt.subplots(1, 2, sharey='all')
    # ax1.plot(x, y)
    # ax1.set_title('Sharing Y axis')
    # ax2.scatter(x, y)
    #
    # # 创建四个子图 -- 图4
    # fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
    # axs[0, 0].plot(x, y)
    # axs[1, 1].scatter(x, y)
    #
    # # 共享 x 轴
    # plt.subplots(2, 2, sharex='col')
    #
    # # 共享 y 轴
    # plt.subplots(2, 2, sharey='row')
    #
    # # 共享 x 轴和 y 轴
    # plt.subplots(2, 2, sharex='all', sharey='all')
    #
    # # 这个也是共享 x 轴和 y 轴
    # plt.subplots(2, 2, sharex='all', sharey='all')
    #
    # # 创建10 张图，已经存在的则删除
    # fig, ax = plt.subplots(num=4, clear=True)
    #
    # plt.show()

    # Matplotlib 散点图
    # 我们可以使用 pyplot 中的 scatter() 方法来绘制散点图。

    # x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    # y = np.array([1, 4, 9, 16, 25, 36, 49, 64])
    # sizes = np.array([20, 10, 60, 20, 20, 20, 20, 80])
    # colors = ['red', 'green', 'black', 'orange', 'purple', 'beige', 'cyan', 'magenta']
    # plt.scatter(x, y, s=sizes, c=colors)
    #
    # x_1 = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
    # y_1 = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
    # plt.scatter(x_1, y_1, color='#88c999')
    # plt.show()

    # x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
    # y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
    # colors = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80])
    # plt.scatter(x, y, c=colors, cmap='afmhot_r')
    # plt.colorbar()
    # plt.show()

    # # 绘制柱状图
    # x = np.array(['hello', 'world', 'thanks', 'no'])
    # y = np.array([10, 12, 3, 5])
    # # plt.bar(x, y)
    # # plt.barh(x, y, height=0.1)  # 横向
    #
    # plt.show()

    # # 饼图
    # y = np.array([10, 15, 3, 8])
    # plt.pie(y, labels=['A', 'B', 'C', 'D'], colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"],
    #         explode=(0, 0.1, 0, 0), autopct='%.2f%%')
    # plt.title('这是一个么得感情的饼图')
    # plt.show()
    # x = linspace(-np.pi, np.pi, 256)
    # c, s = np.cos(x), np.sin(x)
    # plt.plot(x, c)
    # plt.plot(x, s)
    # plt.show()

    # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
    figure(figsize=(8, 6), dpi=80)
    subplot(1, 1, 1)

    x = np.linspace(-np.pi, np.pi, 256)
    c, s = np.cos(x), np.sin(x)

    plot(x, c, color='blue', linewidth=1.5, linestyle='-', label='cosine')
    plot(x, s, color='yellow', linewidth=1.5, linestyle='-', label='sine')

    legend(loc='upper left')
    # 设置轴的上下限 以及 记号
    xlim(x.min() * 1.1, x.max() * 1.1)
    # xticks(np.linspace(-4, 4, 9))
    xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])

    ylim(s.min()*1.1, s.max()*1.1)
    yticks([-1, 0, 1],
           [r'$-1$', r'$0$', r'$1$'])

    # 以分辨率 72 来保存图片
    # savefig('image_1.png', dpi=72)

    # 设置图片边界
    # plt.xlim(s.min() * 1.1, s.max() * 1.1)
    # plt.ylim(c.min() * 1.1, c.max() * 1.1)

    # xmin, xmax = x.min(), x.max()
    # # ymin, ymax = Y.min(), Y.max()
    # #
    # # dx = (xmax - xmin) * 0.2
    # # dy = (ymax - ymin) * 0.2
    # #
    # # xlim(xmin - dx, xmax + dx)
    # # ylim(ymin - dy, ymax + dy)

    # 移动脊柱 把 x y 轴放在中间的位置上 画一个平面直角坐标系

    ax = gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))

    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    # show()

    # 添加图例
    # plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
    # plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")
    #
    # legend(loc='upper left')

    # 给特殊点做注释
    t = 2 * np.pi / 3
    plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle='--')
    scatter([t, ], [np.cos(t)], 50, color='blue')

    annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data', xytext=(+10, +30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))

    plot([t, t], [0, np.sin(t)], color='red', linewidth=2.5, linestyle='--')
    scatter([t, ], [np.sin(t)], 50, color='blue')

    annotate(r'$\sin(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data', xytext=(-90, -50),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
    show()
    pass


if __name__ == '__main__':
    main()
    pass
