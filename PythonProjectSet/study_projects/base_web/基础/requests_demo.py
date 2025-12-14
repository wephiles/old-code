# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/13 013 13:30
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/requests_demo.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

# import requests
# import json
#
# page_count = 1
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.306"
# }
#
# while True:
#     print("第一页:")
#     url = r"https://www.chinaunicom.com.cn/43/menu01/1/column05?pageNo={}&pageSize=10&year=2023&month=11".format(page_count)
#
#     response = requests.get(url=url, headers=headers)
#     page_count += 1
#     if not response.text.strip():
#         break
#     print(response.text)
#      # json.loads(response.text)


# import json
# import requests
#
#
# def jsonp_queryMoreNums(data_dict):
#     print(data_dict)
#
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#                   "(KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.306"
# }
# url = "http://num.10010.com/NumApp/NumberCenter/qryNum?callback=jsonp_queryMoreNums&provinceCode=11&cityCode=110&advancePayLower=0&sortType=1&goodsNet=4&searchCategory=3&qryType=02&channel=B2C&numNet=186&groupKey=1203791326&judgeType=1&_=1713017778636"
#
# response = requests.get(url=url, headers=headers)
#
# eval(response.text)

# import requests
# from bs4 import BeautifulSoup
#
# url = r"https://www.autohome.com.cn/news/"
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#                   "(KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.306"
# }
# # GBK 编码
# response = requests.get(url=url, headers=headers)
# data = response.content.decode("GBK")
#
# # 整个HTML字符串
# soup_obj = BeautifulSoup(data, "html.parser")
# news_area_obj = soup_obj.find(name="div", attrs={"id": "auto-channel-lazyload-article"})  # find是找一个
# li_obj_list = news_area_obj.find_all(name="li", attrs={})
#
# for li_obj in li_obj_list:
#     # li标签利，下面寻找p标签 如果没找到p标签 返回None
#     p_obj = li_obj.find(name="p")  # 包含很多东西的对象
#
#     if not p_obj:
#         continue
#     # 获取p标签内部的字符串
#     print(p_obj.text)

import requests
import pprint
from bs4 import BeautifulSoup

url = r"https://www.autohome.com.cn/news/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.306"
}
# GBK 编码
response = requests.get(url=url, headers=headers)
data = response.content.decode("GBK")

# 整个HTML字符串
soup_obj = BeautifulSoup(data, "html.parser")
editor_area_obj = soup_obj.find(name="div", attrs={"class": "editor-wrap"})
editor_li_list = editor_area_obj.find_all(name="li")

all_editor_msg = dict()
for li_obj in editor_li_list:
    editor_url = li_obj.find(name="a").attrs["href"]
    editor_img_url = li_obj.find(name="img").attrs["src"]
    editor_name = li_obj.find(name="div", attrs={"class": "editorname"}).text

    all_editor_msg[editor_name] = {"editor_url": editor_url, "editor_img_url": editor_img_url}

pprint.pprint(all_editor_msg)


# --END--
