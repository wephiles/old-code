# -*- coding: utf-8 -*-
# @CreateTime : 2023/3/10 22:18
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/协程coroutine.py
# @Description : 协程 爬虫
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/JinYu-2023?tab=repositories


import asyncio


async def request(url: str = None):  # async修饰的函数 调用之后返回一个协程对象
    print('请求数据', url)
    print('请求成功', url)
    return url

c = request('https://www.baidu.com')

# # 创建一个事件循环对象
# loop = asyncio.get_event_loop()
#
# # 注册协程对象到loop中 然后启动事件循环loop
# loop.run_until_complete(c)

# # task 使用
# loop = asyncio.get_event_loop()
# # 基于loop创建了任务对象task
# task = loop.create_task(c)
# print(task)
#
# loop.run_until_complete(task)
# print(task)

# # feature
# loop = asyncio.get_event_loop()
#
# future = asyncio.ensure_future(c)
# print(future)
#
# loop.run_until_complete(future)
# print(future)


# 绑定回调
def callback(task):
    print(task.result())
    # result 返回的是任务对象中封装的协程对象对应函数的返回值--request的返回值


loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
# 绑定
task.add_done_callback(callback)
loop.run_until_complete(task)  # 绑定到loop中时执行定义的callback函数

# END
