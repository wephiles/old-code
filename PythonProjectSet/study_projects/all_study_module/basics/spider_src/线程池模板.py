# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/5 22:47
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : 线程池模板.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

import os  # 文件操作
import time  # 计算运行时间
import requests  # 爬取网络资源
from lxml import etree  # 数据解析
from multiprocessing.dummy import Pool  # 线程池


if __name__ == '__main__':
    begin = time.perf_counter()  # 开始计时
    # UA伪装
    headers_ = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        #               'AppleWebKit/537.36 (KHTML, like Gecko) '
        #               'Chrome/96.0.4664.45 Safari/537.36'
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.107 Safari/537.36 HBPC/11.0.8.301'
    }
    list_ = []
    # 爬取页面的详情数据
    for item in range(1, 11):
        url_ = 'https://www.3gbizhi.com/tupian/pic1383_' + str(item) + '.html'
        response_ = requests.get(url=url_, headers=headers_).text  # 爬取页面的文字信息
        tree = etree.HTML(response_)
        image_url_ = tree.xpath('//div[@id="showimg"]/a/img/@src')[0]  # 数据解析，解析到图片的url
        image_name_ = image_url_.split('/')[-1]  # 用url最后一个 / 之后的名字作为图片的名字
        list_.append([image_name_, image_url_])    # 将解析到的文件名信息和图片的url保存到一个二维列表里面
    # 新建一个文件夹，保存图片
    if not os.path.exists('image'):
        os.mkdir('image')

    # 保存文件的函数

    def save_image(list_):
        print('Save images...')
            # 获取二进制图片数据
        response_content = requests.get(url=list_[1], headers=headers_).content
        with open('image/' + list_[0], 'wb') as fp:  # 保存二进制文件数据
            fp.write(response_content)
    # print(list_)
    # 开辟一个大小为10的线程池
    pool = Pool(10)
    pool.map(save_image, list_)  # 传入参数，让系统自己执行
    # save_image(list_)
    pool.close()
    pool.join()
    end = time.perf_counter()
    print('Thread Pool - Time: ', end - begin)
    pass
