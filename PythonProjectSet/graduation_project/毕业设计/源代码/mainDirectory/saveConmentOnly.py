# -*- coding: utf-8 -*-
# @CreateTime : 2023/2/22 9:52
# @Author : 20866
# @IDE : PyCharm
# @File : PycharmProject/saveConmentOnly.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://gitee.com/qiongjulingjun

import xlwings as xw


def main() -> int:
    data_list = []
    comment_list = []
    i = 0
    with open('../dictTextDirectory/CourseComment.txt', 'r', encoding='utf8') as fp:
        while True:
            data = fp.readline()
            data_line = data.replace('\n', '')
            if data_line == '':
                break
            data_list.append(data_line)

    for data_ in data_list:
        comment = ''
        data_ = eval(data_)
        for item in data_:
            comment += item + '|'
        comment_list.append(comment)

    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False

    work_book = app.books.open('data_comment.xlsx')
    work_sheet = work_book.sheets['sheet1']
    work_sheet.range('A1').value = 'CourseComments'

    i = 2
    for item in comment_list:
        sheet_txt = 'A' + str(i)
        work_sheet.range(sheet_txt).value = item
        i += 1

    work_book.save()
    work_book.close()
    app.quit()
    print('OK')
    return 0


if __name__ == '__main__':
    main()

# END
