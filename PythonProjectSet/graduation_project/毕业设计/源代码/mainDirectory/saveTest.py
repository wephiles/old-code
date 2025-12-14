# -*- coding: utf-8 -*-
# @CreateTime : 2023/2/20 11:42
# @Author : 20866
# @IDE : PyCharm
# @File : PycharmProject/saveTest.py
# @Description : 说明文件功能
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://gitee.com/qiongjulingjun


def main() -> int:
    comment = ''
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
    # data_list: list[ [str], [str] ] str: '[str, str]'
    for data_ in data_list:
        data_ = eval(data_)
        for item in data_:
            comment += item + ' | '
        comment_list.append(comment)
        comment = ''
    print(len(comment_list))
    print(comment_list)
    return 0


if __name__ == '__main__':
    main()

# END
