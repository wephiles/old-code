# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/1 21:46
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : coroutine_more_task.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# 本文件测试多任务协程

import time
import asyncio


async def request(url):
    print('Download now: ', url)
    # 在异步协程中，如果出现和同步模块相关的代码，就无法实现异步
    # time.sleep(2)  # 本语法是同步模块的语法
    await asyncio.sleep(2)  # 基于异步模块的代码，是个阻塞操作，如果遇到阻塞操作，必须进行手动挂起
    print('Download successfully! ', url)


if __name__ == '__main__':
    start = time.perf_counter()
    urls = [
        'https://www.baidu.com',
        'https://www.Buweishi.com',
        'https://www.wangqi.com'
    ]
    # 任务列表：需要存放多个任务对象
    task_list = []
    for url in urls:
        c = request(url)
        task = asyncio.ensure_future(c)
        task_list.append(task)

    loop = asyncio.get_event_loop()
    # 需要将任务列表封装到wait中
    loop.run_until_complete(asyncio.wait(task_list))
    end = time.perf_counter()
    print('Time: ', end - start)
    pass
