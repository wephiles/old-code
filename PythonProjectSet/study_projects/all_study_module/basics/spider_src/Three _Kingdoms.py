# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/27 21:17
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : Three _Kingdoms.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# 爬取三国演义小说所有的章节标题和所有的章节内容

import requests
from bs4 import BeautifulSoup


def main():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36'
    }
    title_list = []
    page_text_list = []
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text_no = requests.get(url=url, headers=headers)
    page_text_no.encoding = 'utf-8'
    page_text = page_text_no.text
    # 在首页中解析出标题和详情页的url
    soup = BeautifulSoup(page_text, 'lxml')
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('../data_files/Three_Kingdoms.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.a.string
        title_list.append(title)
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        detail_page_text_no = requests.get(url=detail_url, headers=headers)
        detail_page_text_no.encoding = 'utf-8'
        detail_page_text = detail_page_text_no.text
        soup_next = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = soup_next.find('div', class_='chapter_content')
        content = div_tag.text
        page_text_list.append(content)
        fp.write(li.a.string + '' + content + '\n')
        print(title, '爬取成功')
        pass


if __name__ == '__main__':
    main()
