# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/23 22:36
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : html_all.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# 本文件主要爬取所有的HTML文档，并存放在word.txt里面

import requests
import os


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36'
    }
    for i in range(0, 250, 25):
        params = {
            'start': str(i),
            'filter': ''
        }
        url = 'https://movie.douban.com/top250?start=' + str(i) + '&filter='
        response = requests.get(url=url, params=params, headers=headers).text
        with open('../data_files/word.txt', 'a', encoding='utf-8') as fp:
            fp.write(response)
    fp.close()





