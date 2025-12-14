# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/24 15:23
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : get_url_movie.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# 本文件用于抓取所有电影的链接信息

import re
import requests


def get_url_movie():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36'
    }
    ex_url_movie = '<div class="hd">.*?<a href="(.*?)" class'
    url_movie_list = []
    for i in range(0, 250, 25):
        params = {
            'start': str(i),
            'filter': ''
        }
        url = 'https://movie.douban.com/top250?start=' + str(i) + '&filter='
        response = requests.get(url=url, params=params, headers=headers).text
        url_movie = re.findall(ex_url_movie, response, re.S)
        url_movie_list.extend(url_movie)
    return url_movie_list


# get_url_movie()




