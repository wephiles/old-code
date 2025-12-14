# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/14 18:00
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : no_header.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

import time
from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions  # 实现规避检测


if __name__ == '__main__':
    # 实现无头浏览器（无可视化浏览器） phantomjs,已经停止和维护了
    options_chrome = Options()
    options_chrome.add_argument('--headless')
    options_chrome.add_argument('--disable-gpu')

    # 规避检测
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])

    s = Service(r'./chromedriver.exe')
    browser = webdriver.Chrome(service=s, chrome_options=options_chrome, options=options_chrome)

    url_ = 'https://www.baidu.com'
    browser.get(url=url_)
    print(browser.page_source)



    time.sleep(2)
    browser.quit()
    pass
