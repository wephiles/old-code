# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/13 21:24
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : selenium_project_example.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# 本文件是个selenium项目案例
# 实现模拟登录QQ空间 并且自动发说说

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
# from selenium.webdriver import ActionChains


if __name__ == '__main__':
    """
     这是一个selenium的学习相关代码
     这是一个项目案例，实现QQ空间的自动登录
     """
    # 实例化一个浏览器对象，（传入浏览器的驱动程序）
    s = Service(r'./chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    url_ = 'https://qzone.qq.com/'
    driver.get(url=url_)
    driver.maximize_window()
    sleep(1)

    # 我们发现“账号密码登录”是属于iframe标签的！所以要用动作链
    driver.switch_to.frame('login_frame')  # 切换作用域
    a_tag = driver.find_element(By.ID, 'switcher_plogin')
    a_tag.click()

    # 找到输入账号文本框和输入密码的文本框
    user_name_tag = driver.find_element(By.ID, 'u')
    sleep(1)
    # 录入账号 密码
    user_name_tag.send_keys('2086689759')
    sleep(0.5)
    user_password_tag = driver.find_element(By.ID, 'p')
    sleep(1)
    user_password_tag.send_keys('WarmDou_TS0807')
    sleep(0.5)
    # 找到登录按钮，点击
    login_button = driver.find_element(By.ID, 'login_button')
    login_button.click()
    sleep(2)

    # 退出iframe域：
    # driver.switch_to.default_content()

    # 发说说：先点击说说文本发送框
    text_say = driver.find_element(By.ID, '$1_substitutor_content')
    text_say.click()
    sleep(2)
    # 还需要切换框架，但是网上的代码没有用！！！

    # element = driver.find_element(By.CSS_SELECTOR, 'iframe.app_canvas_frame')
    # 点击说说tab，发说说
    driver.find_element(By.ID, '$1_content_content').send_keys('hahahhahahahhahahahha')
    sleep(1)
    driver.find_element(By.ID, '$1_content_content').send_keys('我们总要努力，')
    sleep(1)
    driver.find_element(By.ID, '$1_content_content').send_keys('我们总要拼命向前！')
    sleep(1)
    driver.find_element(By.ID, '$1_content_content').send_keys('——毛泽东 《湘江评论》')
    sleep(1)
    driver.find_element(By.ID, '$1_content_content').send_keys('\n666666666666666')
    sleep(1)
    # driver.find_element(By.LINK_TEXT, '发表').click()  # 正确发送
    # driver.find_element(By.CLASS_NAME, 'btn-post gb_bt  evt_click').click()  # 错误，找不到
    # driver.find_element(By.CLASS_NAME, 'btn-post').click()  # 正确发送
    # # 我们发现其实如果class中间用空格分开，那么只要写空格隔开的其中一个即可
    # text_say.send_keys('我们总要努力，')
    # sleep(1)
    # text_say.send_keys('我们总要拼命向前！')
    # sleep(1)
    # text_say.send_keys('——毛泽东，湘江评论')
    # sleep(1)

    # 所有操作完成1秒之后关闭浏览器
    sleep(2)

    driver.quit()  # 关闭浏览器

    print('OK')
    pass
