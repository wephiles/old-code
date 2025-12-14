# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/16 016 10:37
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/demo16_多任务异步案例-flask测试.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import asyncio
import requests
import time
import aiohttp

# from website import index_bobo, index_jay, index_tom

urls = [
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom',
]

start = time.time()


async def get_page(url):
    print('downloading...', url)

    # # request发起的请求是基于同步的
    # response = requests.get(url)

    # 基于异步的网络请求模块发起请求 -- aiohttp
    async with aiohttp.ClientSession() as session:
        # 可能阻塞的操作必须await手动挂起
        # post get方法 headers params/data同requests
        async with await session.get(url) as response:
            # text()返回字符串形式的响应数据
            # read()返回二进制数据
            # json()返回json对象数据
            # 获取数据的时候也要挂起
            page_text = await response.text()
    print('over.', page_text)
    return url


futures = []

for url in urls:
    c = get_page(url)
    future = asyncio.ensure_future(c)
    futures.append(future)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))

end = time.time()


print('time: ', end-start)

# --END--
