# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/2/19 20:54:31
# @Project: Pycharm_Project_Set
# @File : insert sort.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

def insert_sort(list_data: list[int]) -> list:
    if len(list_data) <= 1:
        return list_data
    else:
        # 所有数都需要插入一遍
        for i in range(0, len(list_data)):
            # 等待插入的这个元素的前一个元素的下标，这个元素需要和后一个元素比较
            pre_offset = i - 1

            # 标记，表示等待插入的这个元素，这个标记只能是元素，不能是偏移，因为在while循环里面偏移位置会改变
            sign_num = list_data[i]
            # print(sign_num is list_data[i])
            while pre_offset >= 0 and sign_num < list_data[pre_offset]:
                # 直到前一个元素下标等于零，往前移动寻找插入位置
                list_data[pre_offset + 1] = list_data[pre_offset]
                # 同时pre_offset减一
                pre_offset -= 1
                # 找到合适的插入位置，将这个数插入即可
            list_data[pre_offset+1] = sign_num
        return list_data


if __name__ == '__main__':
    test_list = [5, 4, 3, 2, 1]
    print(insert_sort(test_list))
    pass
