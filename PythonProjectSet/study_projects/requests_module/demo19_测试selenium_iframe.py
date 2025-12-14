# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/16 016 16:19
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/demo19_测试selenium_iframe.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
# 实现无头浏览器 导入Options
from selenium.webdriver.chrome.options import Options
# 规避检测 导入ChromeOptions
from selenium.webdriver import ChromeOptions
import time

# 实现无头
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(options=option)

# 无头浏览器 phantomjs/Options
browser.get('https://www.baidu.com/')
print(browser.page_source)
time.sleep(2)
browser.quit()

# --END--
