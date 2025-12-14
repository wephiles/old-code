# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/29 20:59
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : second_hand_housing.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# 本文件爬取58二手房的相关信息

from lxml import etree
import requests


def main():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36'
    }
    url = 'https://tianshui.58.com/ershoufang/'
    # 老规矩，爬取整个页面数据
    response = requests.get(url=url, headers=headers).text
    # 数据解析
    # parser = etree.HTMLParser(encoding='utf-8')  # 使用HTML解析，防止用XML解析出现检测出HTML文档有错误、
    # 不规范的情况，目前来看好像不用这个东西
    tree = etree.HTML(response)
    title_list = tree.xpath('//div[@class="property-content-title"]/h3/text()')
    with open('../data_files/second_hand_housing.txt', 'w', encoding='utf-8') as fp:
        for items in title_list:
            fp.write(items + '\n')
    pass


if __name__ == '__main__':
    main()
