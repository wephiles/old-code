# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/1 22:09
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : coroutine_crawler_real_war.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# 使用 aiohttp 模块中的session对象 ClientSession
import requests
from lxml import etree
import aiohttp
import asyncio
import time
import os

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/97.0.4692.71 Safari/537.36'
    }


def get_urls_names():
    name_list_all = []
    url_list_all = []
    for page_num in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start=' + str(page_num) + '&filter='
        page_text = requests.get(url=url, headers=headers).text
        tree_name = etree.HTML(page_text)
        url_list = tree_name.xpath('//ol[@class="grid_view"]/li/div[@class="item"]//a/img/@src')
        url_list_all.extend(url_list)

        tree_url = etree.HTML(page_text)
        name_list = tree_url.xpath('//ol[@class="grid_view"]/li/div[@class="item"]//a/img/@alt')
        name_list_all.extend(name_list)
    return name_list_all, url_list_all


async def save_images(url):
    tuple_name_url = get_urls_names()
    name_list_all = tuple_name_url[0]

    # if len(name_list_all) == len(url_list_all) and len(name_list_all) == 250:
    for items in range(0, len(name_list_all)):
        # response = requests.get(url, headers=headers).content
        async with aiohttp.ClientSession() as session:
            # todo:在写下面的语句的时候，记得用await挂起
            async with await session.get(url=url, headers=headers) as response:
                # todo:在写下面的语句的时候，记得用await挂起
                page_content = await response.read()
                with open('image/' + name_list_all[items] + '.jpg', 'wb') as fp:
                    print('Save ' + name_list_all[items] + ' ...')
                    fp.write(page_content)
                    fp.close()
    # else:
    #     print('ListLengthError!')


if __name__ == '__main__':
    start = time.perf_counter()
    print(get_urls_names())
    if not os.path.exists('image'):
        os.mkdir('image')
    tuple_name_url = get_urls_names()
    url_list_all = tuple_name_url[1]
    # print(url_list_all)
    futures = []
    print('Save images now, please wait... ')
    for url in url_list_all:
        c = save_images(url)
        future = asyncio.ensure_future(c)
        futures.append(future)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))

    end = time.perf_counter()
    print('Total time: ', end - start)
    pass
