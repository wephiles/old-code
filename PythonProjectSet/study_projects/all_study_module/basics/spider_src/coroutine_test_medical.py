# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/1 21:02
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : coroutine_test_medical.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# 本文件测试:协程

import asyncio


async def request(url):
    print('正在请求的url是:', url)
    print('请求成功', url)
    return url


if __name__ == '__main__':
    # async修饰的函数，返回的一个协程对象
    c = request('https://www.baidu.com')  # c是该函数返回的一个协程对象

    # # 创建一个事件循环对象loop
    # loop = asyncio.get_event_loop()
    #
    # # 将协程对象注册到事件loop中，启动事件循环
    # loop.run_until_complete(c)  # 注册（还可以启动循环对象）

    # # task的使用
    # loop = asyncio.get_event_loop()
    # # 返回一个task事物对象 基于loop创建一个task任务对象
    # task = loop.create_task(c)
    # print(task)
    # # 运行结果：<Task pending name='Task-1' coro=<request() running at \接下一行
    # D:\Pycharm_Project_Set\爬虫学习-哔哩哔哩\coroutine_test_medical.py:17>>
    # loop.run_until_complete(task)
    # print(task)
    # # 正在请求的url是: https://www.baidu.com
    # # 请求成功 https://www.baidu.com
    # # <Task finished name='Task-1' coro=<request() done,    \接下一行
    # # defined at D:\Pycharm_Project_Set\爬虫学习-哔哩哔哩\coroutine_test_medical.py:17> result=None>

    # # future 的使用
    # loop = asyncio.get_event_loop()
    #
    # future = asyncio.ensure_future(c)
    # print(future)
    # loop.run_until_complete(future)
    # print(future)

    # 绑定回调：

    def call_back(future):  # 定义一个回调函数
        # result 返回任务对象中封装的协程对象对应函数的返回值
        print(future.result())

    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(c)
    future.add_done_callback(call_back)
    loop.run_until_complete(future)
    pass
