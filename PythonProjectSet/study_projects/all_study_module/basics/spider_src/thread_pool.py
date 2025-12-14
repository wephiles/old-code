# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/31 21:45
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : thread_pool.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

import time

# 导入线程池模块对应的类
from multiprocessing.dummy import Pool

# 下面是基于单线程串行的执行方式


# def get_page(string):
#     print('downloading...', string)
#     time.sleep(2)
#     print('download successful!', string)
#
#
# if __name__ == '__main__':
#     # 使用单线程串行方式执行：
#     name_list = ['bu', 'wei', 'shi', 'heng', 'shuai']
#     start = time.perf_counter()
#     for i in range(len(name_list)):
#         get_page(name_list[i])
#     end = time.perf_counter()
#     print('time:', end-start)
#     pass

# 下面是基于线程池的方式：


def get_page(string):
    print('downloading: ', string)
    time.sleep(2)
    print('download successful! ', string)


if __name__ == '__main__':
    # 使用单线程串行方式执行：
    start = time.perf_counter()
    name_list = ['bu', 'wei', 'shi', 'heng', 'handsome']

    # 实例化一个线程对象：.
    pool = Pool(5)  # 开辟了五个线程对象

    # 利用进程池处理：
    pool.map(get_page, name_list)  # 将列表元素中的每一个列表元素交给get_page这个阻塞方法进行处理，
    # map的返回值也是get_page这个函数的返回值，map的返回值一定是个列表
    end = time.perf_counter()
    print('time:', end-start)
    pass
