# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/13 20:51
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : selenium_test_runoob.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

# 本文件测试selenium控制iframe

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains
# 上面的语句导入动作链


if __name__ == '__main__':
    """
     这是一个selenium的学习相关代码
     本文件用于爬取淘宝上的相关信息
     """
    # 实例化一个浏览器对象，（传入浏览器的驱动程序）
    s = Service(r'./chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    url_ = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    driver.get(url=url_)

    # 定位到需要拖动到的小方块的标签上面
    driver.switch_to.frame('iframeResult')  # 切换浏览器标签定位的作用域，默认是外部大的HTML标签里面
    # 注意这个参数，driver.switch_to.frame('iframeResult') 里面的字符串是iframe标签的id
    div = driver.find_element(By.ID, 'draggable')

    # 拖动这个小方块：使用动作链
    action = ActionChains(driver)
    # 点击并且长按指定的标签
    action.click_and_hold(div)

    for i in range(0, 10):
        # perform()立即执行动作链操作,move_by_offset()要传入两个参数，第一个是x，水平方向。第二个是y，竖直方向
        action.move_by_offset(25, 0).perform()
        sleep(0.3)
    # 释放动作链
    action.release().perform()
    sleep(1)

    # 点击弹出的警告，点确定
    driver.switch_to.alert.accept()

    # 所有操作完成三秒之后关闭浏览器
    sleep(3)
    driver.quit()  # 关闭浏览器
    pass
