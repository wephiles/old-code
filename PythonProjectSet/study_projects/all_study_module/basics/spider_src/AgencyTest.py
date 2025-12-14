# -*- coding: utf-8 -*-
# @CreateTime : 2023/3/9 21:57
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/AgencyTest.py
# @Description : 测试 python爬虫-代理
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/JinYu-2023?tab=repositories

# 代理：破解封IP这种反爬  代理指的是代理服务器
# 本机IP: 111.164.183.85天津市天津西青 联通

import requests

url = 'https://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0'
}

page_text = requests.get(url=url, headers=headers, proxies={'http': '202.109.157.62'}).text

with open(r'Result/ip1.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)

# END
