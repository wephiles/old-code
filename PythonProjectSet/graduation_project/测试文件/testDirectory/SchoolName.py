# -*- coding: utf-8 -*-
# @CreateTime : 2023/2/14 16:46
# @Author : 20866
# @IDE : PyCharm
# @File : PycharmProject/SchoolName.py
# @Description : 说明文件功能
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://gitee.com/qiongjulingjun

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
import solution_class


def get_school_name() -> list:
    path = Service(
            '毕业设计/毕业设计/chromedriver_win32/chromedriver.exe')  # 浏览器驱动程序地址
    driver = webdriver.Chrome(service=path)
    driver.maximize_window()  # 最大化窗口
    driver.implicitly_wait(10)  # 等待时间超过10s时，抛出异常

    school_name_list = []

    # 打开页面
    pro = solution_class.GetText(driver=driver)  # 实例化类
    pro.open_url(url='https://www.icourse163.org/')
    pro.search_key(pro, '操作系统')
    time.sleep(1)

    for i in range(0, 2):
        school_name = pro.get_school_name(pro)
        school_name_list = school_name_list + school_name

        try:
            pro.jump_next(pro)
        except Exception as e:
            print(f'End of the page: {e}')
    return school_name_list


if __name__ == '__main__':
    name_list = get_school_name()
    with open('SchoolName1.txt', 'w', encoding='utf-8') as fp:
        for item in name_list:
            fp.write(item)
            fp.write('\n')
    print('school name save successfully.')

# END
