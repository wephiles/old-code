# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/14 014 12:28
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/demo5_糗百图片.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.


import requests
import json
import re

if __name__ == '__main__':
    # url = "https://pic.3gbizhi.com/uploads/20240612/8bb1246c67b21da426529660d0a2a52b.png"
    # # UA伪装
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    #                   '(KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.310',
    # }
    # # content返回的是二进制数据
    # response = requests.get(url=url, headers=headers).content
    #
    # file_name = "./data/" + url.split("/")[-1]
    # with open(file_name, "wb") as fp:
    #     fp.write(response)
    #     print(file_name, "保存成功")

    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.310',
    }

    for k in range(1, 26):
        url = "https://desk.3gbizhi.com/deskMV/index_{}.html".format(k)
        # url = "https://www.3gbizhi.com/wallMV/index_{}.html".format(k)
        # 获取当前url的页面文本数据
        page_text = requests.get(url, headers=headers).text
        # 聚焦爬虫 解析数据

        """
        <li class="box_black">
            <a href="https://desk.3gbizhi.com/deskMV/3668.html" class="desk imgw" target="_blank">
                <img src="https://pic.3gbizhi.com/uploads/20240613/295dbfc6c219d98ea80845f5bbdfb795.jpg" alt="听音乐的女生，侧躺在床边的短裤，美腿美女桌面壁纸图片" style="height: 182px;">
                <div class="title">听音乐的女生，侧躺在床边的短裤，美腿美女桌面壁纸图片</div>
            </a>
            <div class="tips">
                                <a href="https://desk.3gbizhi.com/tag/dazhangtui/">大长腿</a>
                                <a href="https://desk.3gbizhi.com/tag/nvsheng/">女生</a>
                                <a href="https://desk.3gbizhi.com/tag/chuangbian/">床边</a>
                                <a href="https://desk.3gbizhi.com/tag/bainenmeizi/">白嫩妹子</a>
                                <a href="https://desk.3gbizhi.com/tag/duanku/">短裤</a>
                                <a href="https://desk.3gbizhi.com/tag/meitui/">美腿</a>
                                <a href="https://desk.3gbizhi.com/tag/meitun/">美臀</a>
                                <a href="https://desk.3gbizhi.com/tag/yinyue/">音乐</a>
                            </div>
        </li>
        """
        ex = r'<li class="box_black">.*?lay-src="(.*?)" alt.*?</li>'
        url_list = re.findall(ex, page_text, re.S)  # re.S单行匹配 re.M多行匹配
        for item in url_list:
            file_name = "./data/images/" + item.split("/")[-1]
            img_content = requests.get(item, headers=headers).content
            with open(file_name, "wb") as fp:
                fp.write(img_content)
                print(file_name, "下载完成！")
# --END--
