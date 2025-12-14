# -*- coding: utf-8 -*-
# @CreateTime : 2024/5/7 007 20:04
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/demo1.py
# @Description : 读取CSV文件，下载图片保存
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/99.0.4844.84 "
                  "Safari/537.36 HBPC/12.1.3.306"
}

with open("mv.csv", "r", encoding="utf-8") as fp:
    # 表头,忽略
    fp.readline()

    # 读取每一行数据
    for line in fp:
        _, user_name, url = line.strip().split(",")

        # 下载图片
        print("Downloading images ...")
        response = requests.get(url=url, headers=headers)

        # 保存图片
        save_path = r"./assets/{}.png".format(user_name)
        with open(save_path, "wb") as file_obj:
            print("Saving image", user_name + "png", "...")
            file_obj.write(response.content)

# --END--
