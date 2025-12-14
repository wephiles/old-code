# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/14 19:13
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : selenium模板.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


if __name__ == '__main__':
    options_chrome = Options()
    options_chrome.add_argument('--headless')
    options_chrome.add_argument('--disable-gpu')

    s = Service(r'./chromedriver.exe')
    browser = webdriver.Chrome(service=s, options=options_chrome)

    url_ = 'https://www.baidu.com'
    browser.get(url=url_)
    time.sleep(3)
    image_tag = browser.find_element(By.CLASS_NAME, 'mnav')
    time.sleep(0.5)
    image_tag.click()
    time.sleep(2)

    page_text = browser.find_element(By.TAG_NAME, 'html').text
    print(page_text)

    time.sleep(2)
    browser.quit()
    pass
