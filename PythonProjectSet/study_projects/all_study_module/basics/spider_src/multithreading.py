# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/3 22:15
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : multithreading.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

import os
import time
import requests
from lxml import etree
from multiprocessing.dummy import Pool


if __name__ == '__main__':
    begin = time.perf_counter()
    headers_ = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        #               'AppleWebKit/537.36 (KHTML, like Gecko) '
        #               'Chrome/96.0.4664.45 Safari/537.36'
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.107 Safari/537.36 HBPC/11.0.8.301'
    }
    list_ = []
    for item in range(1, 11):
        url_ = 'https://www.3gbizhi.com/tupian/pic1383_' + str(item) + '.html'
        response_ = requests.get(url=url_, headers=headers_).text
        tree = etree.HTML(response_)
        image_url_ = tree.xpath('//div[@id="showimg"]/a/img/@src')[0]
        image_name_ = image_url_.split('/')[-1]
        list_.append([image_name_, image_url_])
    if not os.path.exists('image'):
        os.mkdir('image')
    def save_image(list_):
        for items in list_:
            print('Downloading image ' + list_[0] +' ...Please wait! ')
            response_content = requests.get(url=list_[1], headers=headers_).content
            print('Save image: ' + list_[0] + ' ... Please wait! ')
            with open('image/' + list_[0], 'wb') as fp:
                fp.write(response_content)
    # print(list_)

    pool = Pool(10)
    pool.map(save_image, list_)
    # save_image(list_)
    pool.close()
    pool.join()
    end = time.perf_counter()
    print('Thread Pool - Time: ', end - begin)
    pass
