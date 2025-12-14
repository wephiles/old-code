# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/11 22:13
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : honor_skins.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe]

import requests
from lxml import etree
# import re


if __name__ == '__main__':
    # ex = '<font class="skcolor_ljg">华为</font>.*?"(.*?)".*?</em>'
    url = 'https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA&enc=utf-8&pvid=73c4d7c2ad81404da965796bd86dfbfa'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    price = tree.xpath('//div[@class="p-price"]/strong/i/text()')
    # print(price)
    print(len(price))

    # name_goods = re.findall(ex, page_text, re.S)
    # print(name_goods)

    name_goods = tree.xpath('//div[@class="p-name p-name-type-2"]/a/em/text()')
    # print(name_goods)
    print(len(name_goods))

    num_evaluation = tree.xpath('//div[@class="gl-i-wrap"]//div[@class="p-commit"]/strong/a[@id="J_comment_100022491874"]/text()')
    print(len(num_evaluation))
    print(num_evaluation)
    pass
