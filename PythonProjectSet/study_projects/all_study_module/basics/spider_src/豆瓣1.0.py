# -*- coding: utf-8 -*-
# @CreateTime : 2021/11/29 14:27
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : 豆瓣1.0.py
# @Software : PyCharm

# from bs4 import BeautifulSoup
import requests
import json


def main():
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'start': '0',  # 从第几部电影开始取
        'limit': '20',  # 一次请求取出的个数
        'action': 'None'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.107 Safari/537.36 HBPC/11.0.8.300'
    }
    # data = {
    #
    # }
    response = requests.get(url=url, params=param, headers=headers)
    list_data = response.json()
    fp = open('./douban.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
    print('Over!!!')
    pass


if __name__ == '__main__':
    main()





