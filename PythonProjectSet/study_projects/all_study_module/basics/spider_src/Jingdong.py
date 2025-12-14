# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/3 20:41
# @Author : 20866
# @Site : 
# @Project: 爬虫学习-哔哩哔哩
# @File : Jingdong.py
# @Software : PyCharm

import requests
from bs4 import BeautifulSoup


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36'
    }
    param = {
        'callback': 'fetchJSON_comment98',
        'productId': '100015451172',
        'score': '0',
        'sortType': '5',
        'page': '0',
        'pageSize': '10',
        'isShadowSku': '0',
        'fold': '1'
    }
    url = 'https://club.jd.com/comment/productPageComments.action'
    # ?callback=fetchJSON_comment98&productId=100015451172&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
    page_text = requests.get(url=url, params=param, headers=headers).text
    page_text_beautiful = BeautifulSoup(page_text, 'lxml')
    print(page_text_beautiful.prettify())
    pass


if __name__ == '__main__':
    main()















