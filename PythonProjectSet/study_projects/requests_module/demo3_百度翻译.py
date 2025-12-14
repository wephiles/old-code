# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/14 014 10:51
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/demo3_百度翻译.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import requests
import json

if __name__ == '__main__':

    url = "https://fanyi.baidu.com/sug"
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.310',
    }
    # 输入关键字
    keywords = input("请输入要翻译的文本: >>> ")
    # 传入的数据
    data = {
        "kw": keywords,
    }
    # 发送请求 获取返回的数据
    response = requests.post(url=url, data=data, headers=headers)
    # 直接返回一个字典对象 如果确认服务器响应数据是json类型的，就可以用json这个方法
    dict_obj = response.json()
    file_name = "./data/{}.json".format(keywords)
    with open(file_name, "w", encoding="utf-8") as fp:
        json.dump(dict_obj, fp=fp, ensure_ascii=False)
        print(file_name, "存储成功")

# --END--
