# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/31 17:15
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : progress_bar_test.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# 本文件用于测试python进度条

import time
from tqdm import tqdm
import sys
from progressbar import *


def progress_bar_first():
    # 第一种进度条：不需要库，就是一个看起来是进度条其实不是的一个进度条
    print('程序启动中，请稍候...')
    for i in range(26):
        a = '·' * i
        b = '□' * (25 - i)
        c = (i / 25) * 25 * 4
        print('\r{}{}{:.2f}%'.format(a, b, c), end='')
        time.sleep(0.1)
    print('\nEnd!')


def progress_bar_second(percent, start_str='', end_str='', total_length=0):
    bar = ''.join(["\033[41m%s\033[41m" % '   '] * int(percent * total_length)) + ''
    bar = '\r' + start_str + bar.ljust(total_length) + ' {:0>4.1f}%|'.format(percent*100) + end_str
    print(bar, end='', flush=True)


def progress_bar_third():
    # 第三种进度条：
    print('程序启动中，请稍候...')
    print('正在下载......')
    for i in range(11):
        if i != 10:
            sys.stdout.write('||')
        else:
            sys.stdout.write('||'+str(i*10)+'%/100%')
        sys.stdout.flush()
        time.sleep(0.3)
    print('\n下载成功！')


def progress_bar_forth():
    # 第四种进度条：
    print('程序启动中，请稍候...')
    for i in tqdm(range(20)):
        time.sleep(0.5)
    print('over')


def progress_bar_fifth():
    # 第五种进度条：
    print('程序启动中，请稍候...')
    progress = ProgressBar()
    for i in progress(range(100)):
        time.sleep(0.01)


def progress_bar_sixth():
    # 第六种进度条
    print('程序启动中，请稍候...')


if __name__ == '__main__':
    # progress_bar_first()
    # print('程序启动中，请稍候...')
    # for i in range(101):
    #     time.sleep(0.01)
    #     end_str = '100%'
    #     progress_bar_second(i / 100, start_str='', end_str=end_str, total_length=15)
    # progress_bar_third()
    # progress_bar_forth()
    # progress_bar_fifth()
    pass
