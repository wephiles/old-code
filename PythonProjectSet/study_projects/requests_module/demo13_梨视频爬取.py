# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/15 015 15:46
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/demo13_梨视频爬取.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import requests
from lxml import etree
from multiprocessing.dummy import Pool
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.310',
}


def get_content(dic):
    """

    Args:
        dic ():

    Returns:

    """
    data = requests.get(url=dic['url'], headers=headers).text
    print(dic['title'], "正在下载...")
    with open('./data/videos/' + dic['title']+'.html', 'w', encoding='utf-8') as fp:
        fp.write(data)
        print(dic['title'], "下载成功")


def main():
    # 对下面这个网址发请求，解析出视频的网址信息和视频名称
    url = 'https://www.pearvideo.com/category_1'

    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    page_text = response.text

    parser = etree.HTMLParser(encoding='utf-8')
    tree = etree.HTML(page_text, parser=parser)

    ul = tree.xpath('//*[@id="categoryList"]')[0]
    li_list = ul.xpath('./li[@class="categoryem "]')
    urls = []
    for li in li_list:
        url = "https://www.pearvideo.com/" + li.xpath('.//a[@class="vervideo-lilink actplay"]/@href')[0]
        title = li.xpath('.//div[@class="vervideo-title"]/text()')[0]
        # detail_response = requests.get(url=url, headers=headers)
        # detail_response.encoding = detail_response.apparent_encoding
        # detail_page_text = detail_response.text
        dic = {
            'title': title,
            'url': url,
        }
        urls.append(dic)

    pool = Pool(processes=4)
    pool.map(get_content, urls)
    pool.close()
    pool.join()
    pass


if __name__ == '__main__':
    main()

# --END--
