# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/26 9:58
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : get_director.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

import requests
import re
from bs4 import BeautifulSoup


def get_director_name():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36'
    }
    ex_director_name = '<div class="bd">.*?<p class>.*?" (.*?)"'
    director_name_list = []
    for i in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start=' + str(i) + '&filter='
        response = requests.get(url=url, headers=headers).text
        soup = BeautifulSoup(response, 'html.parser')
        # director_name = re.findall(ex_director_name, response, re.S)
        # director_name_list.extend(director_name)
        for items in soup.find_all('div', 'item'):
            director = items.find('div', 'bd').p.contents[0].string
            director.replace(' ', '')
            director.replace('\\n', '')
            director_name_list.append(director)
    print(director_name_list)
    return director_name_list


get_director_name()


