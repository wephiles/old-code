# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/3 20:41
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : video_pa.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

import requests
import os


if __name__ == '__main__':
    url_1 = 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/26/24/360562426/360562426-1-30076.m4s' \
            '?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N0' \
            '3eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1' \
            'mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1641220823&gen=playurlv2&os=cosbv&oi=613325249&trid=' \
            'a27dd500d2bf4d77a29f57d35cb4adb8u&platform=pc&upsig=965ea3cad0ee697eff3cc012dff463d7&uparams=e' \
            ',uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&bvc=vod&nettype=0&orderid=0,3&agrr=0&bw=132333&logo=80000000'
    url_2 = 'https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/26/24/360562426/360562426_nb2-1-30280.m4s' \
            '?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0' \
            'B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0e' \
            'N0B599M=&uipk=5&nbs=1&deadline=1641220823&gen=playurlv2&os=hwbv&oi=613325249&trid=a27dd500d' \
            '2bf4d77a29f57d35cb4adb8u&platform=pc&upsig=3780bc5a3414cf24f82acdd530e102d7&uparams=e,uipk,' \
            'nbs,deadline,gen,os,oi,trid,platform&mid=0&bvc=vod&nettype=0&orderid=0,3&agrr=0&bw=15940&logo=80000000'
    headers_ = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36',
        'referer': 'https://www.bilibili.com/video/BV17q4y1s7UV?from=search&seid=8140084728691964777'
    }
    response_ = requests.get(url=url_1, headers=headers_).content
    response_1 = requests.get(url=url_2, headers=headers_).content
    with open('video_.mp4', 'wb') as fp:
        fp.write(response_)

    with open('video_.mp3', 'wb') as fp:
        fp.write(response_1)

    pass
