# -*- coding: utf-8 -*-
# @CreateTime : 2023/2/17 15:35
# @Author : 20866
# @IDE : PyCharm
# @File : PycharmProject/onePageComment.py
# @Description : 说明文件功能
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://gitee.com/qiongjulingjun


from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
import solution_class


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

    a_list = []
    a_dict = {}
    # 点击某一门课程
    element = pro.driver.find_elements(By.CLASS_NAME, 'f-fcorange.f-ib')[15]
    element.click()
    time.sleep(1)

    pro.second_handle(pro)  # 定位到第二个句柄
    time.sleep(1)

    course_name = pro.get_course_name(pro)
    if course_name != 'None':
        try:
            course_evaluation_button = pro.driver.find_element(
                By.XPATH, '//*[@id="review-tag-button"]')
        except Exception as e:
            print(f'NetworkError: {e}')
        else:
            course_evaluation_button.click()
        while True:  # 一直点击下一页，并爬取每页的数据
            comment_ = pro.get_course_evaluation(pro)
            a_list += comment_
            pro.click_evaluation_next(pro)
            if pro.click_evaluation_next(pro) == 1:
                break
    a_dict[course_name] = a_list
    pro.browser_quit(pro)
    print(a_dict)
    return 0


if __name__ == '__main__':
    main()

# END
