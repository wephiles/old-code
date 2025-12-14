# -*- coding: utf-8 -*-
# @CreateTime : 2024/2/4 004 19:36
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/demo01.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

# def function(data: list[int]):
#     if isinstance(data, list):
#         print(data)
#     else:
#         raise TypeError("the type of args is not true!")
#
#
# function([15])

# print(None)

import os


def contain(string, key):
    """判断一个字符是否在一个字符串里面，一旦有，直接返回True。

    :param string: str 字符串
    :param key: str 需要判断的字符
    :return: bool
    """
    for item in string:
        if item == key:
            return True
    return False


def function(file_path, key):
    """ - 写一个函数
            - 判断一个参数1：字符串(文件路径)是否是存在的，
            - 不存在则返回None，
            - 存在，则读取文件的每一行数据，判断每一行数据是否包含参数2：字符串
                - 在，则将这一行数据追加到列表中
                - 不在，继续读下一行
            - 返回列表，包含字符串的每一行数据
        - 最终自己调用这个函数

    :param file_path: string, the file path.
    :param key: string, which only have one letter.
    :return: list 
    """

    if not os.path.exists(file_path):
        return None
    print_list = []
    with open(file_path, "r", encoding="utf-8") as fp:
        for line in fp:
            if contain(line, key):
                print_list.append(line.strip())
    return print_list


if __name__ == "__main__":
    data_list = function(r"D:\CSProjects\PycharmProjects\studyProject\wupeiqiStudyBilibili\data\my_string.txt", 'a')
    print(data_list)

# END
