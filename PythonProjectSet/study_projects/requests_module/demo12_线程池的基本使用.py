# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/15 015 15:31
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/demo12_线程池的基本使用.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

# # 单线程 串行
# import time


# def get_page(string):
#     print("正在下载", string)
#     time.sleep(3)
#     print('下载成功', string)
#
#
# name_list = ["计科", "aa", "bb", "cc"]
#
# start_time = time.time()
#
# for item in name_list:
#     get_page(item)
#
# end_tile = time.time()
#
# print("time: ", end_tile - start_time)


# 线程池
import time

# 导入线程池模块对应的类
from multiprocessing.dummy import Pool

start_time = time.time()


# 单线程 串行
def get_page(string):
    print("正在下载", string)
    time.sleep(3)
    print('下载成功', string)


name_list = ["计科", "aa", "bb", "cc"]

# 实例化一个线程池对象 创建四个线程 用来放四个阻塞操作
pool = Pool(processes=4)

# 第一个参数是阻塞的操作函数名 第二个参数是个可迭代对象
# 将第二个参数中的每一个元素传递给第一个参数作为参数进行处理 即将后面列表里面的每个值都传进第一个函数里面进行处理
pool.map(get_page, name_list)  # map的返回值就是get_page的返回值


end_time = time.time()

print("time: ", end_time - start_time)

# --END--
