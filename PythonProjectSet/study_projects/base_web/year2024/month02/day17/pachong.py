# -*- coding: utf-8 -*-
# @CreateTime : 2024/2/21 021 17:54
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : testProject/pachong.py
# @Description :
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

import requests
from bs4 import BeautifulSoup

# 豆瓣电影Top250的URL
base_url = 'https://movie.douban.com/top250'

# 发送请求的头部信息，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 存储电影信息的列表
movies = []

# 爬取所有页面的电影信息
for page in range(10):  # 豆瓣Top250共有10页
    url = f'{base_url}?start={page * 25}&filter='
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 解析电影信息
    items = soup.find_all('div', class_='item')
    director_text = ""
    cast_text = ""
    year_text = ""
    for item in items:
        title = item.find('span', class_='title').text.strip()
        director = item.find('p', class_='director')
        if director is not None:
            director_text = director.text.strip()
        cast = item.find('p', class_='cast')
        if cast is not None:
            cast_text = director.text.strip()
        year = item.find('span', class_='year')
        if year is not None:
            year_text = year.text.strip()

        # 存储信息
        movies.append(f'{title}, {director_text}, {cast_text}, {year_text}')

# 将信息保存到文本文件
with open('douban_top250_movies.txt', 'w', encoding='utf-8') as file:
    for movie in movies:
        file.write(movie + '\n')

print('电影信息已保存到douban_top250_movies.txt文件中。')

# END
