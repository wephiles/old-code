# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/2/17 16:50:57
# @Project: Pycharm_Project_Set
# @File : bubble sort.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun


def bubble_sort(list_data: list[int]) -> list:
    """A simple bubble sort."""
    if len(list_data) <= 1:
        return list_data
    else:
        for i in range(0, len(list_data)-1):
            for j in range(0, len(list_data)-1):
                if list_data[j] > list_data[j+1]:
                    list_data[j], list_data[j+1] = list_data[j+1], list_data[j]
        return list_data


def bubble_sort_optimization(list_data: list[int]) -> list:
    """Optimization of bubble sorting."""

    if len(list_data) <= 1:
        return list_data
    else:
        last_exchange_offset = len(list_data) - 1
        sort_border = len(list_data) - 1
        # 比较len(list_data)-1轮
        for i in range(0, len(list_data)-1):
            if_sort_complete = True
            for j in range(0, sort_border):
                if list_data[j] > list_data[j+1]:
                    if_sort_complete = False
                    list_data[j], list_data[j + 1] = list_data[j + 1], list_data[j]
                    last_exchange_offset = j

            # 排序边界，每进行一轮排序都会让一个最大值移到最后面，其可以减少循环的次数，加快排序速度
            # 寻找最后一个交换的位置，下次循环就改为对这个边界以前进行排序
            sort_border = last_exchange_offset

            # 这个判断语句的作用是：如果进行到某一轮，这一轮没有交换则表示在这一轮已经排序完成，可以直接跳出循环
            if if_sort_complete is True:
                break

        return list_data


if __name__ == '__main__':
    a_list = [5, 4, 3, 2, 1]
    print(bubble_sort(a_list))
    print(bubble_sort_optimization(a_list))
