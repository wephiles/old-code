# -*- coding: utf-8 -*-
# @CreateTime : 2023/2/19 15:44
# @Author : 20866
# @IDE : PyCharm
# @File : PycharmProject/saveCourseName.py
# @Description : 说明文件功能
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://gitee.com/qiongjulingjun

import re
import xlwings as xw


def main() -> int:
    with open('../dictTextDirectory/CourseName.txt', 'r', encoding='utf8') as fp:
        a_list = fp.readlines()
    for i in range(0, len(a_list)):
        a_list[i] = a_list[i].replace('\n', '')
        a_list[i] = re.sub(r'[0-9]+', '', a_list[i])

    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False

    wb = app.books.add()
    ws = wb.sheets['sheet1']
    column_id = 100001
    for i in range(2, 35):
        offset = 'A' + str(i)
        ws.range(offset).value = column_id
        column_id += 1
    ws.range('A1').value = 'CourseId'
    ws.range('B1').value = 'CourseName'
    ws.range('C1').value = 'SchoolName'
    ws.range('D1').value = 'CourseScore'
    ws.range('E1').value = 'CourseTime'
    ws.range('F1').value = 'IfFine'
    ws.range('G1').value = 'ParticipateNumber'
    ws.range('H1').value = 'CourseDetail'
    ws.range('I1').value = 'CourseOverview'
    ws.range('J1').value = 'CourseComment'
    wb.save('data.xlsx')

    work_book = app.books.open('data.xlsx')
    work_sheet = work_book.sheets['sheet1']
    i = 2
    for item in a_list:
        sheet = 'B' + str(i)
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
