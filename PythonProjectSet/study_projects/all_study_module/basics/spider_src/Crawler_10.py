# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/1 17:33
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : Crawler_10.py
# @Software : PyCharm

import requests
# from bs4 import BeautifulSoup


def main():
    # 如何爬取图片数据
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36'
    }
    url = 'https://pic.qiushibaike.com/system/pictures/12496/124962107/medium/GV3DEDNYP3I2GUHL.jpg'
    img_data = requests.get(url=url, headers=headers).content  # content返回二进制形式的图片数据
    with open('qiu_tu.jpg', 'wb') as fp:
        fp.write(img_data)
    pass


if __name__ == '__main__':
    main()
