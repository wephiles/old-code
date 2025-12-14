# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/2/20 18:13:57
# @Project: Pycharm_Project_Set
# @File : binary insertion sort.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

def binary_insertion_sort(list_data: list[int]) -> list:
    if len(list_data) <= 1:
        return list_data
    else:
        for i in range(1, len(list_data)):
            sign_number = list_data[i]
            low_offset = 0
            high_offset = i - 1
            # 下面必须是 <= ,不能是<
            while low_offset <= high_offset:
                mid_offset = (low_offset + high_offset) // 2
                if sign_number > list_data[mid_offset]:
                    low_offset = mid_offset + 1
                else:
                    high_offset = mid_offset - 1
            # while 循环完成后，找出了要插入的位置
            for j in range(i-1, high_offset, -1):
                list_data[j+1] = list_data[j]
            list_data[low_offset] = sign_number
            # TODO: 这个程序还需要优化一下，程序运行结果是错误的 2022/02/20 19:25
        return list_data


if __name__ == '__main__':
    test_list = [5, 4, 3, 2, 1]
    print(binary_insertion_sort(test_list))
    pass
