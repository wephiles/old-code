# -*- coding: utf-8 -*-
# @CreateTime : 2023/3/9 22:25
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/HighPerformanceAsynchronous.py
# @Description : 高性能异步爬虫
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/JinYu-2023?tab=repositories


import requests
import re
from multiprocessing.dummy import Pool
from lxml import etree

url = 'https://www.pearvideo.com/category_1'
name_list = []
url_list = []

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0'
}


def multithreading():  # 多进程或者多线程 不建议
    return None


# https://www.pearvideo.com/video_1779481
def get_urls() -> any:
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
    for li in li_list:
        detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
        name = li.xpath('./div/a/div[2]/text()')[0]
        url_list.append(detail_url)
        name_list.append(name+'.mp4')
    return None


def get_response_text(url: str = None) -> any:
    detail_page_text = requests.get(url=url, headers=headers).text
    ex = 'srcUrl="(.*?)",vdoUrl'
    video_url = re.findall(ex, detail_page_text)
    print(video_url)
    return None


def process_pool() -> None:  # 进程池 线程池 线程池处理阻塞且耗时的操作
    # pool = Pool(3)  # 开辟四个线程对象 线程池有四个线程对象
    # pool.map(get_page, name_list)  # 提交给线程池 前一个参数为阻塞的哪一个函数
    return None


def main() -> int:
    get_urls()
    get_response_text(url_list[0])
    return 0


if __name__ == '__main__':
    # 线程池主要代码：
    # pool = Pool(4)
    # poll.map(get_video_data, urls)
    # 其中get_video_data() - 是个慢速阻塞操作 中需要添加一个url参数 urls是网址列表
    # pool.close()
    # pool.join()
    main()

# END
