# -*- codeing = utf-8 -*-
# @Time : 2021/5/30 21:08
# @Auther : 20866
# @Site : 
# @File : Splide_Video.py
# @Software : PyCharm

### 我不去想自己能否成功 既然选择了远方 便只顾风雨兼程！

###  用 python 爬取网站上的视频 并且存到文件夹里

### 豆瓣top250网站：https://movie.douban.com/top250?start=0&filter=

# import requests
# import re       ### 正则表达式 文字匹配
# import xlwt     ###  Excel表格操作
# import xlrd     ###  从Excel表格读取数据
import urllib   ### 指定url 获取网页数据
# import bs4      ### 网页解析 获取数据
# import flask    ###
# import sqlite3  ### Sqlite 数据库操作
# from bs4 import BeautifulSoup


def main():
    baseurl =  "https://movie.douban.com/top250?start="  ###第一页的网页地址
    ### 爬取网页
    datalist = GetData(baseurl)
    ### 逐一解析数据
    ### 保存数据
    savepath = r"豆瓣电影top250.xls"
    saveData(savepath)
    askUrl(baseurl)
    return 1

###爬取网页


def GetData(baseurl):
    datalist = []
    for i in range(0,10):
        url = baseurl + str(i * 25)
        html = askUrl(url)
    ### 逐一解析数据
    return datalist


def saveData(savepath):
    print("save......")
    return 1

### 得到一个指定url的网页内容


def askUrl(url):
        head = { ###模拟浏览器头部信息 向浏览器发送消息 （请求）
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
        } ###用户代理 表示告诉豆瓣服务器 我们是什么机器 本质上是告诉浏览器 我们可以接受什么水平的文件
        request = urllib.request.Request(url = url , headers = head)### 封装
        html = ""
        try:
            response = urllib.request.urlopen(request) ###发送请求
            html = response.read().decode("utf-8")
            # print(html)
        except urllib.error.URLError as e:
            if hasattr(e, "code"): ###  出错代码
                print(e.code)
            if hasattr(e, "reason"): ### 出错原因
                print(e.reason)
        return html


if __name__ == "__main__":
    main()
