# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/2/18 19:31:13
# @Project: Pycharm_Project_Set
# @File : select sort.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun


def select_sort(list_data: list[int]) -> list:
    if len(list_data) <= 1:
        return list_data
    else:
        for i in range(0, len(list_data)-1):
            # 首先给最小值的偏移赋初值为0，因为每次循环都需要重新确定下标，所以在外层循环设置
            min_offset = i
            for j in range(i+1, len(list_data)):
                if list_data[j] < list_data[min_offset]:
                    min_offset = j
            if i != min_offset:
                # 要注意这一点，要是最小值不等于偏移为min_offset才发生交换，减少交换次数
                list_data[min_offset], list_data[i] = list_data[i], list_data[min_offset]
        return list_data


if __name__ == '__main__':
    test_list = [5, 4, 3, 2, 1]
    print(select_sort(test_list))
    pass
