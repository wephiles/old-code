# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/5 23:03
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : 单线程 + 协程模板.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

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


def get_all_name_url():
    """
    获取所有的图片的地址
    """
    url_list_all = []
    items_complete_url = []

    for k in range(1, 11):  # 获得1 - 10 页的页面的信息
        url_page = 'https://pic.netbian.com/4kmeinv/index_' + str(k) + '.html'
        page_text = requests.get(url=url_page, headers=headers).text  # 获得文本信息
        tree = etree.HTML(page_text)
        tree_url = tree.xpath('//div[@class="slist"]/ul/li/a/img/@src')  # 解析出图片的地址，在img标签下的src里面
        url_list_all.extend(tree_url)  # 先将所有的图片url保存到一个列表url_list_all里面，用于后续拼接成完整的url

    for items in url_list_all:  # 把网址拼接成一个完整的网址
        items_complete_url_string = 'https://pic.netbian.com' + items
        items_complete_url.append(items_complete_url_string)

    return items_complete_url


async def save_image_content(url_img):
    """
    保存图片数据
    """
    name = url_img.split('/')[-1]  # 从地址中把最后一个带jpg后缀的字符串当做图片的文件名
    print('Save ', name, ' ...')

    async with aiohttp.ClientSession() as session:  # 获取二进制图片数据
        async with await session.get(url=url_img, headers=headers) as response:
            content = await response.read()
    # contents = requests.get(url=url_img, headers= headers).content  # 获取二进制图片数据

    with open('image/' + name, 'wb') as fp:  # 打开文件存放，保存文件
        fp.write(content)  # 给文件内写入二进制数据
        fp.close()  # 关闭文件
        print(name, 'has been saved! ')
    return 0


if __name__ == '__main__':
    begin = time.perf_counter()  # 计算时间

    if not os.path.exists('image'):  # 新建一个文件夹，保存图片
        os.mkdir('image')
    else:
        print('Directory ' + ' "./image" is exists! Please delete it! ')

    url_all_images = get_all_name_url()
    futures = []

    for url_a_image in url_all_images:
        c = save_image_content(url_a_image)  # c是一个函数对象
        future = asyncio.ensure_future(c)  # 将函数c注册到future中
        futures.append(future)  # 将future添加到futures列表中

    loop = asyncio.get_event_loop()  # 事件循环
    loop.run_until_complete(asyncio.wait(futures))

    end = time.perf_counter()
    print('Total time: ', end-begin)
    pass
