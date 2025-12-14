# -*- coding: utf-8 -*-
# @CreateTime : 2021/11/29 14:59
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : 肯德基.py
# @Software : PyCharm

import requests
from bs4 import BeautifulSoup


def main():
    kw = input('Enter the city:')
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36'
    }
    data = {
        'cname': '',
        'pid': '',
        'keyword': kw,
        'pageIndex': '1',
        'pageSize': '10'
    }
    response = requests.post(url=url, data=data, headers=headers)
    page_text = response.text
    page_text = BeautifulSoup(page_text, 'lxml')
    # print(page_text.prettify())
    file_name = kw+'_kfc.html'
    with open('./kfc.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text.prettify())
    print('Over!!!')


if __name__ == '__main__':
    main()



