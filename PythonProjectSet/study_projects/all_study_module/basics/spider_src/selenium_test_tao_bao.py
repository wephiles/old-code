# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/13 20:22
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : selenium_test_tao_bao.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


if __name__ == '__main__':
    """
     这是一个selenium的学习相关代码
     本文件用于爬取淘宝上的相关信息
     """
    # 实例化一个浏览器对象，（传入浏览器的驱动程序）
    s = Service(r'./chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    url_ = 'https://uland.taobao.com/sem/tbsearch'
    driver.get(url=url_)

    # 标签定位
    search_input = driver.find_element(By.ID, 'J_search_key')

    # 标签交互：
    search_input.send_keys('华为')

    # 拖动滚轮，执行一组js程序
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 滚轮向下滚动一屏的高度
    sleep(2)

    # 找到并且点击搜索按钮
    button = driver.find_element(By.CLASS_NAME, 'submit')
    button.click()
    sleep(2)

    driver.get('https://www.baidu.com')
    sleep(2)
    driver.back()  # 回退。就是浏览器左上角的向左的按钮
    sleep(2)
    driver.forward()  # 前进

    # 所有操作完成三秒之后关闭浏览器
    sleep(3)
    driver.quit()  # 关闭浏览器
    pass
