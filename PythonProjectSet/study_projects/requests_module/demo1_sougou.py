# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/14 014 10:25
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/demo1_sougou.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import requests

# 指定url
url = "https://www.sogou.com/"


# 发起请求 get方法会返回一个响应对象
response = requests.get(url=url, headers=headers, params=)

# 获取响应数据 text返回的是字符串形式的数据
text_get = response.text

# 持久化存储
with open("./data/sougou.html", "w", encoding="utf-8") as fp:
    fp.write(text_get)

# --END--
