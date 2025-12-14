# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/31 22:04
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : thread_pool_crawler.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# 利用线程池爬取梨视频网站上的视频数据

import re
import requests
from lxml import etree
from multiprocessing.dummy import Pool


def get_video_data(dic):
    pass


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36'
    }
    # 对下述的url发送请求，解析出视频详情页的url和视频的名称
    url = 'https://www.pearvideo.com/category_59'
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
    ex = 'srcUrl":"(.*?)"}}'
    for li in li_list:
        detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
        name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
        # print(detail_url, name)
        # 对详情页的url发起请求
        detail_page_text = requests.get(url=detail_url, headers=headers).text
        # 从详情页中解析出视频所对应的地址
        video_url = re.findall(ex, detail_page_text)  # video_url存放解析出来的视频的地址
        print(video_url)
    pass
