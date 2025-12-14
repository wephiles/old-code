# -*- coding: utf-8 -*-
# @CreateTime : 2023/2/22 19:50
# @Author : 瑾瑜 20866
# @IDE : PyCharm
# @File : PycharmProject/saveCommentDataStructure.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/JinYu-2023?tab=repositories

import xlwings as xw


if __name__ == '__main__':
    file_path = r'D:\PycharmProject\毕业设计\毕业设计\源代码\dictTextDirectory\CourseCommentDataStructure.txt'
    all_line_txt_list = []
    with open(file_path, 'r', encoding='utf-8') as fp:
        read_list_str = []
        while True:
            one_line = fp.readline()
            one_line_txt = one_line.replace('\n', '')
            if one_line == '':
                break
            read_list_str.append(one_line_txt)
    # read_list_str  是一个字符串 字符串的内容是一个列表 '['', '', '']'
    for item in read_list_str:
        all_line_txt_list.append(eval(item))
    # print(len(all_line_txt_list))  # 长度为33

    one_course_list = []

    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False

    try:
        work_book = app.books.open(r'dataCommentDataStructure.xlsx')
    except Exception as e:
        work_book.save()
        work_book.close()
        app.quit()
        print(f'OpenFileError: {e}')
    else:
        number_count = 2
        work_sheet = work_book.sheets['sheet1']
        for item in all_line_txt_list:
            one_course_list = item

            for element in one_course_list:
                work_sheet.range('A'+str(number_count)).value = element
                number_count += 1
        work_book.save()
        work_book.close()
        app.quit()
        print(number_count)
    print('OK')

# END
