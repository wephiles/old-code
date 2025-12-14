# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/15 23:35:47
# @Author : 20866
# @Site : None
# @Project: Pycharm_Project_Set
# @File : login_12306.py
# @Software : PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options  # 无头浏览器
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions


if __name__ == '__main__':
    """ 
    这是一个模拟登录12306网站的一个程序
    使用selenium模块 
    """

    # 规避检测：
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 加这条语句，也是规避检测，12306就不会检测到我们是selenium登录了
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    service_ = Service(r'./chromedriver.exe')
    browser = webdriver.Chrome(service=service_, options=chrome_options)

    url_ = 'https://www.12306.cn/index/'
    browser.get(url=url_)  # 打开这个页面

    browser.maximize_window()  # 最大化窗口
    sleep(1)

    login_tag = browser.find_element(By.ID, 'J-btn-login')  # 定位到登录按钮并且点击
    login_tag.click()
    sleep(1)

    # 以防万一，先点击账号登录这个标签，定位到账号密码登录
    login_account = browser.find_element(By.XPATH, '//div[@class="login-box"]/ul/li/a')
    login_account.click()
    sleep(1)

    # 找到并且输入账号
    account_number = browser.find_element(By.ID, 'J-userName')
    account_number.send_keys('18822321558')
    sleep(1)

    # 找到并且输入密码
    account_password = browser.find_element(By.ID, 'J-password')
    account_password.send_keys('WarmDou_TS0807')
    sleep(1)

    # 点击登录按钮，进入下一个页面
    login_immediately = browser.find_element(By.CLASS_NAME, 'btn-primary')
    login_immediately.click()
    sleep(1)

    # 先定位到滑块
    # slide_tag = browser.find_element(By.ID, 'nc_1_n1z')
    # action = ActionChains(browser)  # 实例化一个对象
    # action.click_and_hold(slide_tag)  # 点击并且长按
    # for i in range(0, 8):  # 向右水平移动
    #     action.move_by_offset(40, 0).perform()
    #     sleep(0.0005)
    # action.release().perform()
    # 以下代码转载自：https://www.jb51.net/article/192242.htm
    while True:
        try:
            span = browser.find_element(By.ID, 'nc_1_n1z')
            action = ActionChains(browser)
            # 点击长按指定的标签
            action.click_and_hold(span).perform()
            for i in range(0, 5):
                action.move_by_offset(75, 0).perform()
                sleep(0.000000005)
            sleep(1)
            info = browser.find_element(By.XPATH, '//*[@id="J-slide-passcode"]/div/span').text
            # print(info)
            if info == '哎呀，出错了，点击刷新再来一次':
                # 点击刷新
                browser.find_element(By.XPATH, '//*[@id="J-slide-passcode"]/div/span/a').click()
                sleep(0.1)
            # 重新移动滑块
            action.release().perform()
            sleep(1)
        except:
            print('ok!')
            break
    # 点击弹出的警告框里面的确定：
    # browser.switch_to.alert.accept()
    sleep(1)
    accept = browser.find_element(By.CLASS_NAME, 'ok')
    accept.click()
    sleep(1)
    browser.quit()
    print('end')
    pass
