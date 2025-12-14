# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/29 21:47
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : image_second_housing.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# 本文件主要使用xpath爬取一个网站上的图片数据

import requests
import os
from lxml import etree


def main():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Wi n64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36'
    }
    url = 'https://pic.netbian.com/4kbeijing/index.html'
    response = requests.get(url=url, headers=headers).text
    tree = etree.HTML(response)
    image_list = tree.xpath('//div[@class="slist"]//li/a/img/@src')
    if not os.path.exists('image_girl'):
        os.mkdir('image_girl')
    for items in image_list:
        url = 'https://pic.netbian.com/' + items
        img_name = url.split('/')[-1]
        img_content = requests.get(url=url, headers=headers).content
        fp = open('image_girl/' + img_name, 'wb')
        fp.write(img_content)
        fp.close()
        print(img_name, '保存成功！')
    print('图片已全部保存成功！')
    pass


if __name__ == '__main__':
    main()
