# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/21 22:29
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : 糗图爬取.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

import requests
import re
import os
import time


def main():
    begin = time.perf_counter()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36'
    }
    param = {
        '2670efbdd59c7e3ed3749b458cafaa37': ''
    }
    # 空列表 存放解析出来的正则表达式（图片的url）
    response_url_all = []
    # 正则表达式 获取所有图片的链接地址
    ex = '<div class="thumb">.*?<img src="(.*?)" alt'
    # 获取整个页面的网页信息，以便对网页信息进行分析和数据存储
    for k in range(1, 14):
        url = 'https://www.qiushibaike.com/imgrank/page/' + str(k) + '/'
        response_text = requests.get(url=url, params=param).text
        response_url = re.findall(ex, response_text, re.S)
        for items in response_url:
            items = 'https:' + items
            response_url_all.append(items)
            # 已经获取所有的图片的url，存放在一个列表 response_url_all 中
    # print(response_url_all)
    # 新建一个文件夹，存放爬取到的图片的数据
    if not os.path.exists('image'):
        os.mkdir('image')
    for items_image in response_url_all:
        image_name = items_image.split('/')[-1]
        items_date = requests.get(url=items_image, headers=headers).content
        with open('image/' + image_name, 'wb') as fp:
            fp.write(items_date)
        print(image_name, '下载成功！！！')
    end = time.perf_counter()
    print('运行时间:', end - begin)
    # 运行时间: 278.4240219


if __name__ == '__main__':
    main()

# 天津师范大学 卜伟仕 2086689759@qq.com 版权所有







