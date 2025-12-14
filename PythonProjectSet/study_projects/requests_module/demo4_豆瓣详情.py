# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/14 014 11:15
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/demo4_豆瓣详情.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import requests
import json

if __name__ == '__main__':
    url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20"
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.310',
    }

    params = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20',
    }

    response = requests.get(url=url, headers=headers, params=params)
    list_data = response.json()
    with open("./data/douban.json", "w", encoding="utf-8") as fp:
        json.dump(obj=list_data, fp=fp, ensure_ascii=False)
        print("文件下载完毕")

# --END--
