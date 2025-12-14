# -*- coding: utf-8 -*-
# @CreateTime : 2023/2/19 21:51
# @Author : 20866
# @IDE : PyCharm
# @File : PycharmProject/saveParticipate.py
# @Description : 说明文件功能
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://gitee.com/qiongjulingjun


import xlwings as xw


def main() -> int:
    with open('../dictTextDirectory/ParticipateNumber.txt', 'r', encoding='utf8') as fp:
        a_list = fp.readlines()

    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False

    work_book = app.books.open('data.xlsx')

    work_sheet = work_book.sheets['sheet1']

    i = 2
    for item in a_list:
        sheet_txt = 'G' + str(i)
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
