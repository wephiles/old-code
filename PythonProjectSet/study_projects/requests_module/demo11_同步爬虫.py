# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/15 015 15:15
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/demo11_同步爬虫.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.310',
}


def get_content(url):
    print("正在爬取", url)
    # get方法是阻塞的
    response = requests.get(url, headers=headers)
    if response.status_code == '200':
        return response.content
    else:
        return 'error'


def parse_content(content):
    print("数据长度为：", len(content))


def main():
    urls = ["https://bj.58.com/ershoufang/",
            'https://www.baidu.com',
            'https://www.sougou.com']

    for url in urls:
        content = get_content(url)
        parse_content(content)


if __name__ == '__main__':
    main()

# --END--
