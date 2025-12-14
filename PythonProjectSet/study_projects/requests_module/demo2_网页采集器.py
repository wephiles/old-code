# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/14 014 10:34
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/demo2_网页采集器.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.


import requests

if __name__ == '__main__':

    url = "https://www.sogou.com/web"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.310',
    }
    # 处理url携带的参数 -- 封装到字典中
    keywords = input("输入你想搜索的关键字")
    params = {
        'query': keywords,
    }
    # 对指定的url发起的请求是携带参数的 并且请求过程已经处理了参数
    response = requests.get(url=url, params=params, headers=headers)

    page_text = response.text.replace("\n", " ")

    file_name = './data/' + keywords + '.html'
    with open(file_name, 'w', encoding="utf-8") as fp:
        fp.write(page_text)
        print(file_name, "保存成功")

# --END--
