# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/14 014 14:02
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/demo7_三国演义.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.


import requests
from bs4 import BeautifulSoup
import json


def main():
    url = "https://www.shicimingju.com/book/sanguoyanyi.html"
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.310',
    }

    response = requests.get(url=url, headers=headers)
    # response.encoding = 'utf-8'
    response.encoding = response.apparent_encoding
    page_text = response.text
    soup = BeautifulSoup(page_text, 'lxml')

    li_list = soup.select('.book-mulu > ul > li')
    file_name = './data/word/sanguoyanyi.txt'
    with open(file_name, 'a', encoding="utf-8") as fp:
        for li in li_list:
            title = li.a.get_text()
            title_url = 'https://www.shicimingju.com' + li.a.attrs['href']
            response_content = requests.get(url=title_url, headers=headers)
            # response_content.encoding = 'utf-8'
            response_content.encoding = response_content.apparent_encoding
            content_msg = response_content.text
            detail_page_soup = BeautifulSoup(content_msg, 'lxml')
            content = detail_page_soup.find('div',
                                            class_="chapter_content").text.replace("\n",
                                                                                   "").replace(" ",
                                                                                               "").replace(" ", "")
            fp.write(title + "\n")
            fp.write(content + "\n")
            print(title, "下载完成！")


if __name__ == '__main__':
    main()

# --END--
