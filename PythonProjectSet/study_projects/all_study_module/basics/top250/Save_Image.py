# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/23 22:58
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : Save_Image.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# 本文件保存所有的电影图片在根目录下的image文件夹里面

import os
import Get_Url_image
import Get_Name_Movie
import requests


if __name__ == '__main__':
    if not os.path.exists('image'):
        os.mkdir('image')
    if len(Get_Url_image.get_image_url_list()) == len(Get_Name_Movie.get_name_list()):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/96.0.4664.45 Safari/537.36'
        }
        for items in range(0, len(Get_Url_image.get_image_url_list())):
            response = requests.get(url=Get_Url_image.get_image_url_list()[items], headers=headers).content
            with open('image/' + Get_Name_Movie.get_name_list()[items] + '.jpg', 'wb') as fp:
                fp.write(response)
                print(Get_Name_Movie.get_name_list()[items]+'.jpg  download successful！')
    print('All images have been downloaded！')



