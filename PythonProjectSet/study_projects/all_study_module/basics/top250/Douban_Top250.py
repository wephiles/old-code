# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/23 21:30
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : Douban_Top250.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
import re

import requests
import re
import os


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36'
    }
    text_html_every_page = []  # 存放每个页面的所有HTML信息
    ex_find_image_src = '<div class="pic">.*?<img.*?src="(.*?)" class'  # 正则表达式，爬取所有图片，并命名(名字为电影名字)
    image_url_list = []
    # 存放电影名字
    name_movie_list = []
    ex_name_movie = '<div class="hd">.*?class="title">(.*?)</span>'
    if not os.path.exists('image'):  # 新建一个image文件夹，存放图片数据
        os.mkdir('image')

    # 所有的数据的爬取，集中在一个循环语句里面中
    for i in range(0, 250, 25):
        params = {
            'start': str(i),
            'filter': ''
        }
        url = 'https://movie.douban.com/top250?start=' + str(i) + '&filter='
        # 获取所有的页面的HTML信息，并保存在word.txt文件里面
        response = requests.get(url=url, params=params, headers=headers).text
        # 将所有的响应信息存到一个列表中去
        text_html_every_page.append(response)
        # 利用正则表达式抓取所有电影的图片的地址
        url_image = re.findall(ex_find_image_src, response, re.S)
        image_url_list.extend(url_image)  # 抓取所有的电影的图片信息

        name_movie = re.findall(ex_name_movie, response, re.S)
        name_movie_list.extend(name_movie)
    # 测试正则表达式
    # print(image_url_list)
    # print(name_movie_list)
    # 测试图片列表和名字列表的长度是否相等
    # if len(image_url_list) == len(name_movie_list):
    #     print('yes')

        # 打开文件，保存我们所抓取到的HTML文档
    #     with open('word.txt', 'a', encoding='utf-8') as fp:
    #         fp.write(response)
    # fp.close()

    # 测试是否成功抓取成功页面信息并且存放到列表中
    # print(text_html_every_page)
    # 将图片全都保存在
    for items in range(0, len(name_movie_list)):


if __name__ == '__main__':
    main()
