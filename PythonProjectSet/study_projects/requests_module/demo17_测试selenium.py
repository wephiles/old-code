# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/16 016 14:18
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/demo17_测试selenium.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

from selenium import webdriver
from lxml import etree
import time

# 实例化一个webdriver对象 浏览器对象
browser = webdriver.Chrome()
url = 'https://www.nmpa.gov.cn/xxgk/fxjzh/ylqxfxjch/index.html'

# 让浏览器发起一个指定url对应请求
browser.get(url=url)
time.sleep(10)

# 获取当前页面源码数据
page_text = browser.page_source
print(page_text)

# 解析源码数据
parser = etree.HTMLParser(encoding='utf-8')
tree = etree.HTML(page_text, parser=parser)

ul = tree.xpath('/html/body/div[4]/div/div[2]/ul')[0]
li_list = ul.xpath('./li')

titles = []

for li in li_list:
    title = li.xpath('./a/@title')[0]
    titles.append(title)
print(titles)

time.sleep(3)

browser.quit()

# --END--
