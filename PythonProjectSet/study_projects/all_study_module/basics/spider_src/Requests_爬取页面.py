# -*- coding: utf-8 -*-
# @CreateTime : 2021/11/28 23:08
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : Requests_爬取页面.py
# @Software : PyCharm

# 动态网页采集器

import requests
from bs4 import BeautifulSoup


# UA伪装（一种反爬机制）
def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.107 Safari/537.36 '
                      'HBPC/11.0.8.300'
    }
    url = 'https://www.sogou.com/web'
    # 写上 url =  'https://www.sogou.com/web?query=波晓张' 也可以
    # 其中要动态地获取页面，那么就可以删除掉?query=波晓张，其中?可以删除也可以不删除
    # 处理url对应的参数:将url所携带的参数封装到字典中
    kw = input('Enter a wold:')
    param = {
        'query': kw
    }
    # 对指定的url发起请求，对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)  # params是在域名后面动态地拼接参数
    page_text = response.text
    page_text = BeautifulSoup(page_text, 'lxml')
    file_name = kw + '.html'
    with open(file_name, 'w', encoding='utf-8') as fp:
        fp.write(page_text.prettify())
    print('爬取数据结束,' + file_name + '保存成功！！！')


if __name__ == '__main__':
    main()
