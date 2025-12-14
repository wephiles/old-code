# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/23 23:18
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : test1.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

import requests
from lxml import etree


url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.45 Safari/537.36'
}

response = requests.get(url=url, headers=headers).text

tree = etree.HTML(response)

list_name = tree.xpath('//div[class="hd"]/a/span/@href')

print(list_name)





