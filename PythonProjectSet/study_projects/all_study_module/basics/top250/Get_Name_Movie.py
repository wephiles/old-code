# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/23 22:53
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : Get_Name_Movie.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# 本文件抓取所有电影的名字

import requests
from lxml import etree


def get_name_list():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36'
    }
    name_title_list_all = []
    for i in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start=' + str(i) + '&filter='
        response = requests.get(url=url, headers=headers).text
        tree = etree.HTML(response)
        name_title_list = tree.xpath('//div[@class="hd"]/a/span/text()')
        name_title_list_all.extend(name_title_list)
    print(name_title_list_all)
    print(len(name_title_list_all))
    return name_title_list_all


get_name_list()
