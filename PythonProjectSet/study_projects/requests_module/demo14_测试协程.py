# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/16 016 10:02
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/demo14_测试协程.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import asyncio


async def request(url):
    print("正在请求...", url)
    print("请求成功", url)
    return url


# 返回一个协程对象
x = request("http://httpbin.org/get")


# # 创建一个事件循环对象
# loop = asyncio.get_event_loop()
#
# # 将协程对象注册到loop，并启动loop
# loop.run_until_complete(x)

# # task的使用
# loop = asyncio.get_event_loop()
# # 基于loop创建了一个task对象
# task = loop.create_task(x)
# print(task)
# # 将任务对象注册到事件循环中并启动
# loop.run_until_complete(task)
# print(task)

# # future的使用
# loop = asyncio.get_event_loop()
# future = asyncio.ensure_future(x)
# print(future)
# loop.run_until_complete(future)
# print(future)


# 回调函数 当任务对象执行成功之后 将任务对象回调执行call_back这个函数
def callback_func(task):
    # 可以用result()函数返回协程对象的返回值 -- 即上面定义的request函数(注册后成为协程对象)的返回值
    # result返回的就是任务对象中封装的协程对象对应函数的返回值
    print(task.result())


# 绑定回调
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(x)
# 将回调函数绑定到任务对象中
future.add_done_callback(callback_func)
loop.run_until_complete(future)

# --END--
