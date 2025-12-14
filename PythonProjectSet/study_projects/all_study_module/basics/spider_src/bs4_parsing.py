# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/27 19:38
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : bs4_parsing.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# import requests
# import os
from bs4 import BeautifulSoup


def main():
    # 将本地的HTML文档中的数据加载到该对象中
    # fp = open('./化妆品.html', 'r', encoding='utf-8')
    # soup = BeautifulSoup(fp, 'lxml')
    # print(soup)
    # print(soup.div)
    # print(soup.find('div'))  # 等价于soup.div
    # print(soup.find('div', class_='hzbbtm'))
    # print(soup.find_all('a')[1])
    # print(soup.select('.columm'))  # . 代表class(类)选择器 # 代表id选择器
    # print(soup.select('#FileItems'))
    # print(soup.select('#FileItems li')[0])
    # print(soup.select('.hzbbannertxt > a')[0].get_text())
    # print(soup.select('.hzbbannertxt > a')[0].string)
    # print(soup.select('link')[1]['href'])
    pass


if __name__ == '__main__':
    main()
