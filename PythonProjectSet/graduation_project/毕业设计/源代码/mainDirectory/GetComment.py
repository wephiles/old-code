# -*- coding: utf-8 -*-
# @CreateTime : 2023/2/15 15:50
# @Author : 20866
# @IDE : PyCharm
# @File : PycharmProject/GetComment.py
# @Description : 说明文件功能
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://gitee.com/qiongjulingjun


from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
import solution_class
from functools import lru_cache


@lru_cache(maxsize=None)
def course_comment() -> dict:
    """获取评论

    返回： 字典
    """
    path = Service(
            '毕业设计/毕业设计/chromedriver_win32/chromedriver.exe')  # 浏览器驱动程序地址
    driver = webdriver.Chrome(service=path)
    driver.maximize_window()  # 最大化窗口
    driver.implicitly_wait(10)  # 等待时间超过10s时，抛出异常

    # 打开页面
    pro = solution_class.GetText(driver=driver)  # 实例化类
    pro.open_url(url='https://www.icourse163.org/')
    pro.search_key(pro, 'python')
    time.sleep(1)
    all_comment_dict = {}
    j = 0
    for i in range(0, 1):  # 一共三页内容
        all_item = pro.all_course(pro)
        # 每一个课程列表
        for item in all_item:
            pro.first_handle(pro)  # 定位到第一个页柄 以便点击课程
            time.sleep(1)
            item.click()
            time.sleep(1)
            pro.second_handle(pro)  # 定位到第二个页柄 以便获取详细信息
            name_course = str(j) + pro.get_course_name(pro)  # 课程名称获取 为以后修正数据做准备
            j += 1
            if name_course != str(j-1) + 'None':
                text_comment_list = pro.get_course_evaluation(pro)  # 获得一门课程的评论

                # 将评论存入字典 字典的key值是课程名 value值是所有评论组成的列表
                all_comment_dict[name_course] = text_comment_list

            pro.close_page(pro)
        pro.first_handle(pro)
        pro.jump_next(pro)
    return all_comment_dict


if __name__ == '__main__':
    """测试。并且保存文件"""
    comment_dict = course_comment()
    with open('../dictTextDirectory/CourseCommentPython.txt', 'w', encoding='utf-8') as fp:
        for item in comment_dict:
            fp.write(item)
            fp.write(':')
            fp.write(str(comment_dict[item]))
            fp.write('\n')
    print('python课程评论保存成功.')

# END
