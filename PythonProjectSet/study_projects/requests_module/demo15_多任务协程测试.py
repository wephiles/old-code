# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/16 016 10:25
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/demo15_多任务协程测试.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import asyncio
import time


async def request(url):
    print("downloading...")
    # # 在异步协程中 如果出现同步模块相关代码 那么就无法实现异步
    # time.sleep(2)

    # 当在asyncio中遇到阻塞操作必须进行手动挂起
    await asyncio.sleep(2)

    print('over')
    return url + '-message'


urls = ['www.baidu.com',
        'www.sougou.com',
        'www.runoob.com',
        'www.firefox.com']

start = time.time()

# 任务列表 存放多个任务对象
future_list = []
for url in urls:
    c = request(url)
    future = asyncio.ensure_future(c)
    future_list.append(future)

loop = asyncio.get_event_loop()
# 必须将任务列表封装到wait方法中
loop.run_until_complete(asyncio.wait(future_list))

end = time.time()

print('time: ', end - start)
# --END--
