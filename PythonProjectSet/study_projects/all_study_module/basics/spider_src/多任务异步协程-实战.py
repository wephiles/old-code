# -*- coding: utf-8 -*-
# @CreateTime : 2023/3/15 18:53
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/多任务异步协程-实战.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/JinYu-2023?tab=repositories

import asyncio
import requests
import time
import aiohttp

start = time.perf_counter()

urls = ['http://127.0.0.1:5000/xiaobu',
        'http://127.0.0.1:5000/jay',
        'http://127.0.0.1:5000/tom']


async def get_page(url):
    print('正在下载', url)
    # aiohttp: 基于异步的网络请求的模块
    async with aiohttp.ClientSession() as session:
        async with await session.get(url) as response:
            # session.post()发post请求 headers params/data/proxy=""
            # 这儿需要挂起
            page_text = await response.text()
            # text()函数返回字符串形式 read()返回二进制形式的对象 json()返回JSON
            print(page_text)
    # response = requests.get(url)
    print(response.text)
    print('下载完毕', url)

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.perf_counter()

print('time: ', end-start)
# END
