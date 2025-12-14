# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/13 19:49
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : selenium_practice_medical.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# 爬取药监总局的企业名称

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from lxml import etree
from time import sleep


if __name__ == '__main__':
    # 实例化一个浏览器对象，（传入浏览器的驱动程序）
    s = Service(r'./chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    # 编写关于浏览器自动化操作的编程

    # 让浏览器对一个指定的url发送一个请求
    driver.get(url='http://scxk.nmpa.gov.cn:81/xk/')

    # 获取浏览器当前页面的源码数据
    page_text = driver.page_source

    # 解析企业名称
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@id="gzlist"]/li')
    for li in li_list:
        name = li.xpath('./dl/@title')[0]
        print(name)
    sleep(5)
    driver.quit()
    pass
