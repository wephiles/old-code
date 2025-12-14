# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/1 22:34
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : selenium_module_test.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# selenium 模块的基本使用

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# 后面是浏览器的驱动位置，记得在字符串前加r，防止转义字符转义
s = Service(r'D:\Google_Driver\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# 用get打开百度页面
driver.get('http://www.baidu.com')
time.sleep(1)

# 查找页面的设置选项，点击
# driver.find_element_by_link_text('设置')[0].click()  # 此语句已经被废弃，不能使用，要使用find_elements()
driver.find_elements(By.ID, 's-usersetting-top')[0].click()
time.sleep(1)

# 打开设置后找到搜索设置选项，设置为每页显示50条
# driver.find_element_by_link_text('搜索设置')[0].click()  # 此语句已经被废弃，不能使用，要使用find_elements()
driver.find_elements(By.CLASS_NAME, 'setpref')[0].click()
time.sleep(1)


# 选中每页显示50条
driver.find_element(By.ID, 'nr_3').click()
# time.sleep(2)
# m.find_elements(By.XPATH, '//*[@id="nr_3"]/option[3]')[0].click()
# m.find_elements(By.XPATH, './/option[3]')[0].click()
time.sleep(1)

# 点击保存设置
# driver.find_element(By.CLASS_NAME, 'prefpanelrestore setting-btn c-btn c-gap-right-large').click()
d = driver.find_element(By.XPATH, '//div[@id="se-setting-7"]/a[@class="prefpanelgo setting-btn c-btn c-btn-primary"]')
d.click()
time.sleep(1)

# 处理弹出的警告页面 确定accept()和取消dismiss()
driver.switch_to.alert.accept()
time.sleep(2)

# 找到百度的输入框并输入 美女
driver.find_element(By.ID, 'kw').send_keys('美女')
time.sleep(1)

# 点击搜索按钮
driver.find_element(By.ID, 'su').click()
time.sleep(1)

# 在打开的页面中找到 美女-百度图片 这个页面
driver.find_element(By.XPATH, '//div[@class="c-container"]/h3[@class="c-title"]/a/text()').click()
time.sleep(1)
pass
