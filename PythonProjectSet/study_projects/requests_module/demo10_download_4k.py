# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/15 015 14:22
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/demo10_download_4k.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.


import os
import requests
from lxml import etree


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.310',
    }

    start_url_list = ["https://pic.netbian.com/4kmeinv/"]
    for i in range(2, 50):
        start_url_list.append("https://pic.netbian.com/4kmeinv/index_{}.html".format(i))

    for url in start_url_list:
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding
        page_text = response.text

        parser = etree.HTMLParser(encoding='utf-8')
        tree = etree.HTML(page_text, parser=parser)

        li_list = tree.xpath('//ul[@class="clearfix"]/li')
        for li in li_list:
            title = li.xpath('./a/b/text()')[0].strip()
            url_img = "https://pic.netbian.com" + li.xpath('./a/img/@src')[0]
            # if os.path.exists('./data/assets'):
            #     os.mkdir('./data/assets')
            file_name = './data/assets/' + title.replace(" ",
                                                         "·").replace("\n",
                                                                      "").replace("\t",
                                                                                  "").replace("*", "·") + url_img.split('/')[-1]

            img_content = requests.get(url=url_img, headers=headers).content

            with open(file_name, 'wb') as fp:
                fp.write(img_content)
                print(file_name, '下载完成！！！')


if __name__ == '__main__':
    main()

# --END--
