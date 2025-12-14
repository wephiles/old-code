# -*- coding: utf-8 -*-
# @CreateTime : 2023/2/20 11:10
# @Author : 20866
# @IDE : PyCharm
# @File : PycharmProject/saveComment.py
# @Description : 说明文件功能
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://gitee.com/qiongjulingjun


import xlwings as xw


def main() -> int:
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False

    work_book = app.books.open('all_data.xlsx')
    work_sheet = work_book.sheets['sheet1']

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
            comment += item + ' | '
        comment_list.append(comment)

    i = 2
    for item in comment_list:
        sheet_txt = 'J' + str(i)
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
