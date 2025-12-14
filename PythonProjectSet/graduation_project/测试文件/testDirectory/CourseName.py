# -*- coding: utf-8 -*-
# @CreateTime : 2023/2/15 12:03
# @Author : 20866
# @IDE : PyCharm
# @File : PycharmProject/CourseName.py
# @Description : 说明文件功能
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://gitee.com/qiongjulingjun


from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
import solution_class


def get_course() -> list:
    path = Service(
            '毕业设计/毕业设计/chromedriver_win32/chromedriver.exe')  # 浏览器驱动程序地址
    driver = webdriver.Chrome(service=path)
    driver.maximize_window()  # 最大化窗口
    driver.implicitly_wait(10)  # 等待时间超过10s时，抛出异常

    course_list = []

    # 打开页面
    pro = solution_class.GetText(driver=driver)  # 实例化类
    pro.open_url(url='https://www.icourse163.org/')
    pro.search_key(pro, '操作系统')
    time.sleep(1)

    for i in range(0, 2):
        all_item = pro.all_course(pro)

        for item in all_item:
            pro.first_handle(pro)
            time.sleep(1)
            item.click()

            time.sleep(1)
            pro.second_handle(pro)

            time.sleep(1)
            course = pro.get_course_name(pro)
            course_list.append(course)

            time.sleep(1)
            pro.close_page(pro)
        pro.first_handle(pro)
        pro.jump_next(pro)
    return course_list


if __name__ == '__main__':
    course = get_course()
    with open('CourseName.txt', 'w', encoding='utf-8') as fp:
        for item in course:
            fp.write(item)
            fp.write('\n')
    print('course save successfully.')

# END
