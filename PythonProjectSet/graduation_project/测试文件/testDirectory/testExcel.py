# -*- coding: utf-8 -*-
# @CreateTime : 2023/2/19 11:34
# @Author : 20866
# @IDE : PyCharm
# @File : PycharmProject/testExcel.py
# @Description : 说明文件功能
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://gitee.com/qiongjulingjun


import xlwings as xw
import re


def main() -> int:

    # app = xw.App(visible=True, add_book=False)
    # app.display_alerts = False
    # app.screen_updating = False
    #
    # work_book = app.books.open('test.xlsx')
    # sheet = work_book.sheets['sheet1'].range('B1')
    # sheet.value = 'SchoolName'
    #
    # sheet_1 = work_book.sheets['sheet1'].range('C1')
    # sheet_1.value = 'CourseName'
    #
    # work_book.save()
    # work_book.close()
    # app.quit()

    with open('CourseName.txt', 'r', encoding='utf8') as fp:
        a_list = fp.readlines()
    for i in range(0, len(a_list)):
        a_list[i] = a_list[i].replace('\n', '')
        a_list[i] = re.sub(r'[0-9]+', '', a_list[i])

    app = xw.App(visible=True, add_book=False)
    app.display_alerts = False
    app.screen_updating = False

    work_book = app.books.open('test.xlsx')

    work_sheet = work_book.sheets['sheet1']
    i = 2
    for item in a_list:
        sheet = 'C' + str(i)
        work_sheet.range(sheet).value = item
        i += 1

    work_book.save()

    work_book.close()
    app.quit()

    print('OK')
    return 0


if __name__ == '__main__':
    main()

# END
