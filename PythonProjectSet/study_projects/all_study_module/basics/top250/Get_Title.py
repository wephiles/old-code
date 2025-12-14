# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/24 15:41
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : Get_Title.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

import re
import requests


def get_title():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36'
    }
    movie_title_list = []
    movie_title_list_new = []
    ex_title_movie = '<div class="hd">.*?class="title">(.*?)</'
    for i in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start=' + str(i) + '&filter='
        response = requests.get(url=url, headers=headers).text
        movie_name = re.findall(ex_title_movie, response, re.S)
        movie_title_list.extend(movie_name)
    print(movie_title_list)


get_title()
