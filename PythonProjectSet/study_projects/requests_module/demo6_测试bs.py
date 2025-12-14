# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/14 014 13:12
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/demo6_测试bs.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import requests
from bs4 import BeautifulSoup
import json

if __name__ == '__main__':
    # 将本地html中数据加载到对象中
    with open("./test_demo.html", "r", encoding="utf-8") as fp:
        soup = BeautifulSoup(fp, "lxml")
        # print(soup)

        # # 从互联网中获取
        # url = "https://www.3gbizhi.com/wallMV/index_2.html"
        #
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        #                   '(KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.310',
        # }
        # page_text = requests.get(url, headers=headers).text
        # soup = BeautifulSoup(page_text, "lxml")
        # print(soup.a)  # 找到整个文档的第一个a标签
        # print(soup.div)  # 找到整个文档的第一个div标签
        # print(soup.find('div'))
        # print(soup.find('div', id="pageNum"))
        # print(soup.find('a', attrs={'title': '首页'}))

        # print(soup.find_all('a'))  # 返回的是符合要求的所有标签 --- 列表
        # print(soup.select('.tips'))  # 返回的是一个列表 找出所有的
        # print(soup.select('.topmenuc > div > a > img'))
        # print(soup.select('.topmenuc > div > a > img')[0])
        # print(soup.select('.topmenuc > div img'))
        # print(soup.select('.topmenuc > div img')[0])

        # print(soup.a.text)  #
        # print(soup.a.string)  # 只能获取该标签下面直系的文本
        # print(soup.a.get_text())  # 可以获取所有文本内容 不是直系的也可以获取
        # print(soup.a)
        print(soup.a['href'])
        # print(soup.select('.topmenuc > div > a > img')[0]['src'])
# --END--
