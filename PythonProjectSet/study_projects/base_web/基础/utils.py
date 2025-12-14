# -*- coding: utf-8 -*-
# @CreateTime : 2024/2/26 026 10:05
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/utils.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles
import os

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.306'
}


def get_url_image(url_source):
    response_data = requests.get(url=url_source, headers=headers).text
    content_obj = BeautifulSoup(response_data)
    url_img = content_obj.find(name="div", attrs={"class": "pic-wrap"}).find(name="img").attrs["src"]
    return url_img


def download_img(url, file_folder):
    file_name = url.split("/")[-1]
    response_data = requests.get(url=url, headers=headers).content
    if not os.path.exists(file_folder):
        os.makedirs(file_folder)
    file_path = os.path.join(file_folder, file_name)
    with open(file_path, "wb") as fp:
        print("正在保存", file_name, "...")
        fp.write(response_data)
        print(file_name, "保存成功！")

# --END--
