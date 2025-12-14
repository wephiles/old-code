# -*- coding: utf-8 -*-
# @CreateTime : 2024/2/26 026 18:55
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/douban_requests.py
# @Description :
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

import requests
import json

url = ("https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8"
       "&sort=recommend&page_limit=20&page_start=20")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url=url, headers=headers)

data_dict = json.loads(res.text)

for item in data_dict["subjects"]:
    print(item["title"], item["url"])

# --END--
