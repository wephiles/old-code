# -*- coding: utf-8 -*-
# @CreateTime : 2023/2/17 16:02
# @Author : 20866
# @IDE : PyCharm
# @File : PycharmProject/oneCourseComment.py
# @Description : 说明文件功能
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://gitee.com/qiongjulingjun


from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import solution_class
import time





def main() -> int:
    path = Service(
        '毕业设计/毕业设计/chromedriver_win32/chromedriver.exe')  # 浏览器驱动程序地址
    driver = webdriver.Chrome(service=path)
    driver.maximize_window()  # 最大化窗口
    driver.implicitly_wait(10)  # 等待时间超过10s时，抛出异常

    # 打开页面
    pro = solution_class.GetText(driver=driver)  # 实例化类
    pro.open_url(url='https://www.icourse163.org/')
    pro.search_key(pro, '操作系统')
    time.sleep(1)

    # 点击某一个课程
    # elements = driver.find_elements(By.CLASS_NAME, 'f-fcorange.f-ib')
    # elements[0].click()
    pro.click_first_course(pro)
    # 定位到第二个窗口的句柄
    pro.second_handle(pro)
    time.sleep(1)
    pro.click_comment_detail(pro)
    print(pro.get_course_evaluation(pro))
    pro.close_page(pro)
    return 0


if __name__ == '__main__':
    main()

# END
