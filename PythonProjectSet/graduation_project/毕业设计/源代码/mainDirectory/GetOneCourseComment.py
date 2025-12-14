# -*- coding: utf-8 -*-
# @CreateTime : 2023/3/1 19:36
# @Author : 瑾瑜 20866
# @IDE : PyCharm
# @File : PycharmProject/GetOneCourseComment.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/JinYu-2023?tab=repositories


from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from lxml import etree
from selenium import webdriver
import solution_class


def get_comment_one_course(url: str = None) -> list[str]:
    path = Service(
        '毕业设计/毕业设计/chromedriver_win32/chromedriver.exe')  # 浏览器驱动程序地址
    driver = webdriver.Chrome(service=path)
    driver.maximize_window()  # 最大化窗口
    driver.implicitly_wait(10)  # 等待时间超过10s时，抛出异常

    # 打开页面
    pro = solution_class.GetText(driver=driver)  # 实例化类
    pro.open_url(url=url)
    time.sleep(2)

    comment_button = pro.driver.find_element(By.ID, 'review-tag-button')
    comment_button.click()
    time.sleep(2)

    list_comment_python = pro.get_course_evaluation(pro)
    pro.driver.close()
    return list_comment_python


if __name__ == '__main__':

    begin = time.perf_counter()

    # url_list = ['https://www.icourse163.org/course/NJU-1001571005?from=searchPage&outVendor=zw_mooc_pcssjg_',
    #             'https://www.icourse163.org/course/HENANNU-1003544138?from=searchPage&outVendor=zw_mooc_pcssjg_',
    #             'https://www.icourse163.org/course/PKU-1003479006?from=searchPage&outVendor=zw_mooc_pcssjg_',
    #             'https://www.icourse163.org/course/NJUE-1462480181?from=searchPage&outVendor=zw_mooc_pcssjg_',
    #             'https://www.icourse163.org/course/PKU-1460924165?from=searchPage&outVendor=zw_mooc_pcssjg_',
    #             'https://www.icourse163.org/course/SUDA-1206947804?from=searchPage&outVendor=zw_mooc_pcssjg_',
    #             'https://www.icourse163.org/course/XIYOU-1003118004?from=searchPage&outVendor=zw_mooc_pcssjg_']

    url_list = ['https://www.icourse163.org/course/BIT-1001870002?from=searchPage&outVendor=zw_mooc_pcssjg_',
                'https://www.icourse163.org/course/SZJM-1466718185?from=searchPage&outVendor=zw_mooc_pcssjg_',
                'https://www.icourse163.org/course/BIT-1001873001?from=searchPage&outVendor=zw_mooc_pcssjg_',
                'https://www.icourse163.org/course/HIT-9003?from=searchPage&outVendor=zw_mooc_pcssjg_',
                'https://www.icourse163.org/course/ZIIT-1002924007?from=searchPage&outVendor=zw_mooc_pcssjg_',
                'https://www.icourse163.org/course/CCEC-1449771164?from=searchPage&outVendor=zw_mooc_pcssjg_',
                'https://www.icourse163.org/course/ZJU-1206456840?from=searchPage&outVendor=zw_mooc_pcssjg_',
                'https://www.icourse163.org/course/BIT-1001870001?from=searchPage&outVendor=zw_mooc_pcssjg_',
                'https://www.icourse163.org/course/NEU-1002127001?from=searchPage&outVendor=zw_mooc_pcssjg_',
                'https://www.icourse163.org/course/BIT-1002058035?from=searchPage&outVendor=zw_mooc_pcssjg_',
                'https://www.icourse163.org/course/NHDX-1463126169?from=searchPage&outVendor=zw_mooc_pcssjg_',
                'https://www.icourse163.org/course/BIT-1001871001?from=searchPage&outVendor=zw_mooc_pcssjg_',
                'https://www.icourse163.org/course/JNU-1463154168?from=searchPage&outVendor=zw_mooc_pcssjg_',
                'https://www.icourse163.org/course/HEBEU-1205998803?from=searchPage&outVendor=zw_mooc_pcssjg_']
    all_list = []
    i = 0
    for url in url_list:
        a_list = get_comment_one_course(url)
        all_list += a_list
        with open('pythonComment_1.txt', 'w', encoding='utf-8') as fp:
            for line in all_list:
                fp.write(line)
                fp.write('\n')
                i += 1
    end = time.perf_counter()
    print('共有 ', i, ' 条数据。 ')
    print('time: ', end - begin)

# END
