# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/3 19:53
# @Author : 20866
# @Site : 
# @Project: 爬虫学习-哔哩哔哩
# @File : Crawler_11.py
# @Software : PyCharm

import re
import requests
import os


def main():
    url = 'https://www.qiushibaike.com/imgrank/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36'
    }
    if not os.path.exists('Embarrassments'):
        os.mkdir('Embarrassments')
    page_text = requests.get(url=url, headers=headers).text
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list = re.findall(ex, page_text, re.S)
    # print(img_src_list)
    for items in img_src_list:
        # 拼接一个完整的图片地址
        items = 'https:' + items
        # 请求到了图片的二进制数据
        image_data = requests.get(items, headers=headers).content
        # 生成图片名称
        image_name = items.split('/')[-1]
        image_path = 'Embarrassments/' + image_name
        with open(image_path, 'wb') as fp:
            fp.write(image_data)
            print(image_name, '下载成功')
    print('爬取数据完成！！！')


if __name__ == '__main__':
    main()




