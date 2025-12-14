# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/14 014 12:18
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/unicome_demo.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

import re
import requests
from bs4 import BeautifulSoup
from pprint import pprint

import utils

# 标题 用户名 喜欢的人数 日期

url = r"https://www.douban.com/group/explore"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.306"
}

response = requests.get(url=url, headers=headers)
data = response.content.decode("utf-8")

content_obj = BeautifulSoup(data, "html.parser")
div_communication = content_obj.find(name="div", attrs={"class": "article"})
div_obj_list = div_communication.find_all(name="div", attrs={"class": "channel-item"})

all_data_dict = dict()

for div_obj in div_obj_list:
    title = div_obj.find(name="h3").find(name="a").text
    user_name = div_obj.find(name="div", attrs={"class": "source"}).find(name="a").text

    like_num_str = div_obj.find(name="div", attrs={"class": "likes"}).text
    like_num = int(re.findall(r"\d+", like_num_str)[0])

    date_time = div_obj.find(name="span", attrs={"class": "pubtime"}).text
    all_data_dict[title] = {"user_name": user_name, "like_num": like_num, "date_time": date_time}
    url_img_obj = div_obj.find(name="div", attrs={"class": "pic-wrap"})
    if not url_img_obj:
        continue
    url_img = url_img_obj.find(name="img").attrs["src"]
    utils.download_img(url_img, "./images")
# pprint(all_data_dict)

# --END--
