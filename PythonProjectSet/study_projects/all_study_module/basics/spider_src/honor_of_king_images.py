# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/11 21:45
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : honor_of_king_images.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# 爬取王者荣耀全皮肤高清图片
import requests

url = 'https://pvp.qq.com/web201605/js/herolist.json'
response = requests.get(url).json()
# print(response)

for i in range(len(response)):
    ename = response[i]['ename']
    cname = response[i]['cname']
    title = response[i]['title']
    if response[i]['skin_name'] is None:
        print(ename,cname,title)
    else:
        skin_name = response[i]['skin_name'].split('|')
        print(ename, cname, title, skin_name)

        for i in range(1, len(skin_name)+1):
            img_url = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg'.format(ename,ename,i)
            picture = requests.get(img_url).content
            with open('D:/clawer/hero_skins/'+cname+skin_name[i-1]+'.jpg', 'wb') as f:
                f.write(picture)
                print('正在下载'+skin_name[i-1]+'皮肤')
