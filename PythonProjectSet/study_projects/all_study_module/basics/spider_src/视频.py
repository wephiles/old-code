# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/31 16:47
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : 视频.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# 带进度条的python爬虫程序设计

import requests
import sys


def download_video(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; '
                      'Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    n = 1
    print('Get video...')
    response = requests.get(url=url, headers=headers, stream=True)
    content_size = int(response.headers['content-length'])
    print('Save video...')
    with open(r'D:\音乐免费下载\video.mp4', 'wb') as fp:
        for i in response.iter_content(chunk_size=1024):
            rate = n * 1024 / content_size
            print('下载进度:{0:%}'.format(rate))
            fp.write(i)
            n += 1
    print('Save successfully!!!')


x = 'https://vd2.bdstatic.com/mda-kj4yfs92s40w3v2s/v1-cae/mda-kj4yfs92s40w3v2s.mp4'
download_video(x)
