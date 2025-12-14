# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/6 0:00
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : 多任务协程.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

import asyncio
# import requests
import time
import aiohttp


async def a_function(url):
    # print('d n')
    # # time.sleep(2)
    # await asyncio.sleep(2)

    print('downloading ', url)
    # response = requests.get(url=url)
    # 使用基于异步的网络请求的模块：aiohttp模块 使用ClientSession类中的session对象
    # session.post()方法发起post请求
    # headers参数的添加 和串行的是一样的params data /还可以设置代理IP proxy = 'https://ip:port'
    async with aiohttp.ClientSession() as session:
        async with await session.get(url=url) as response:
            # todo: 在使用协程的时候要记得使用异步的方法，同时要对相关的操作做挂起！！！
            # text()方法返回字符串数据 read()方法返回二进制数据 json()返回json对象
            page_text = await response.text()  # 一定要手动挂起！！！
            print(page_text)
    print('over ', url)
    pass


if __name__ == '__main__':
    # start = time.perf_counter()
    # urls = ['www', 'eee', 'rrr']
    # # 任务列表：存放多个任务对象
    # futures = []
    #
    # for  url in urls:
    #     c = a_function(url)
    #     future = asyncio.ensure_future(c)
    #     futures.append(future)
    # loop = asyncio.get_event_loop()
    #
    # loop.run_until_complete(asyncio.wait(futures))  # 固定语法，需要将任务列表封装到wait()中
    # print(time.perf_counter() - start)

    # 模拟真实爬虫——flask服务器相关的信息访问
    start = time.perf_counter()
    urls = ['http://127.0.0.1:5000/bo_bo', 'http://127.0.0.1:5000/jay', 'http://127.0.0.1:5000/tom']
    futures = []
    for url in urls:
        c = a_function(url)
        future = asyncio.ensure_future(c)
        futures.append(future)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))

    end = time.perf_counter()
    print(end - start)
    pass
