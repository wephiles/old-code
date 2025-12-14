# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/15 015 13:58
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/demo9_58二手房.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import requests
from lxml import etree


def main():
    url = "https://bj.58.com/ershoufang/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.310',
    }

    page_text = requests.get(url, headers=headers).text

    parser = etree.HTMLParser(encoding='utf-8')
    tree = etree.HTML(page_text, parser=parser)

    div_list = tree.xpath('//div[@tongji_tag="fcpc_ersflist_gzcount"]')
    with open("./data/ershoufang.txt", 'a', encoding='utf-8') as fp:
        for div in div_list:
            title = div.xpath('./a//div[@class="property-content-title"]/h3/text()')[0]
            fp.write(title.strip() + '\n')
            print(title.strip(), "保存成功！")


if __name__ == '__main__':
    main()

# --END--
