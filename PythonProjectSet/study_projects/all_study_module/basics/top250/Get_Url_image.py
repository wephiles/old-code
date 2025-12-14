# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/23 22:46
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : Get_Url_image.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# 本文件抓取所有电影的图片路径
import re
import requests


def get_image_url_list():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/96.0.4664.45 Safari/537.36'
    }
    ex_image_url = '<div class="pic">.*?<img.*?src="(.*?)" class'  # 正则表达式，爬取所有图片，并命名(名字为电影名字)
    url_image_list = []
    for i in range(0, 250, 25):
        params = {
            'start': str(i),
            'filter': ''
        }
        url = 'https://movie.douban.com/top250?start=' + str(i) + '&filter='
        response = requests.get(url=url, params=params, headers=headers).text
        url_image = re.findall(ex_image_url, response, re.S)
        url_image_list.extend(url_image)
    return url_image_list


# get_image_url_list()



