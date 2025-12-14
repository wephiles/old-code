# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/16 016 15:08
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/demo18_测试selenium01.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

# import requests
#
# url = 'https://liuyan.people.com.cn/v1/threads/list/df'
# params = {
#     'appCode': "PC42ce3bfa4980a9",
#     'param': '{"fid":"593","showUnAnswer":1,"typeId":5,"lastItem":"","position":"0","rows":10,"orderType":2}',
#     'signature': "a7db9282e68f7ccceff0785b444c2194",
#     'token': "",
# }
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
#     'Referer': 'https://liuyan.people.com.cn/threads/list?checkStatus=0&fid=593&formName='
#                '%E7%94%98%E8%82%83%E7%9C%81%E5%A7%94%E4%B9%A6%E8%AE%B0%E8%83%A1%E6%98%8C%E5%8D%87'
#                '&position=0&province=42&city=&saveLocation=4&pForumNames=%E7%94%98%E8%82%83%E7%9C%81',
#     'Cookie': '__jsluid_s=b6f99a7ef8c99463f8247582d8bedcaf; language=zh-CN; Hm_lvt_40ee6cb2aa47857d8ece9594220140f1=1718521516; deviceId=8e219f1c-4672-46f3-8756-17771ba0ba60; Hm_lpvt_40ee6cb2aa47857d8ece9594220140f1=1718521577',
# }
#
# response = requests.post(url=url, headers=headers)
# print(response.text)

# 上面方式访问被拦截了！！！

# 用selenium
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# selenium打开浏览器
browser = webdriver.Chrome()

# 窗口最大化
browser.maximize_window()

# 访问要爬取的页面
browser.get('https://www.baidu.com')
# browser.get('https://www.sougou.com')

# # 获取页面数据
# page_text = browser.page_source

# browser.find_element(By.ID, 'kw').send_keys('瑾瑜')
browser.find_element(By.CLASS_NAME, 's_ipt').send_keys('瑾瑜')

# browser.find_element(By.NAME, 'wd').send_keys('瑾瑜')
# browser.find_element(By.XPATH, '//*[@id="kw"]').send_keys('瑾瑜')

browser.find_element(By.ID, 'su').click()
time.sleep(1)

browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# print(browser.current_url)
# print(browser.window_handles)
# print(browser.current_window_handle)
# print(browser.title)
# time.sleep(3)

# # 刷新页面
# browser.refresh()
browser.get('https://www.sougou.com')
time.sleep(1)
browser.back()
time.sleep(1)
browser.forward()
# 关闭浏览器和驱动
browser.quit()

# --END--
