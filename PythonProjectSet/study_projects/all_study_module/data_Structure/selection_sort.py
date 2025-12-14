# -*- coding: utf-8 -*-
# @CreateTime : 2023/7/16 016 22:14
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/selection_sort.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles

# 选择排序

a_list = [0, 98, 94, 2, 4, -12, 19, 50, 48, 19, -100]


def selection_sort(test_list: [int]) -> [int]:
    if len(test_list) == 0:
        return []
    for i in range(0, len(test_list) - 1):
        min_index = i
        for j in range(i + 1, len(test_list)):
            if test_list[j] < test_list[min_index]:
                min_index = j
        if i != min_index:
            test_list[i], test_list[min_index] = test_list[min_index], \
                                                 test_list[i]
    return test_list


def selection_sort_optimize(test_list: [int]) -> [int]:
    begin = 0
    end = len(test_list) - 1
    while begin < end:
        min_offset = begin
        max_offset = end
        # i = begin + 1
        # while i <= end:
        #     if test_list[i] < test_list[min_offset]:
        #         min_offset = i
        #     if test_list[i] > test_list[max_offset]:
        #         max_offset = i
        #     i += 1

        # 上面注释的代码功能同样可以实现
        for i in range(begin + 1, end + 1):
            while i <= end:
                if test_list[i] < test_list[min_offset]:
                    min_offset = i
                if test_list[i] > test_list[max_offset]:
                    max_offset = i
                i += 1
        if begin != min_offset:
            test_list[begin], test_list[min_offset] = test_list[min_offset], \
                                                      test_list[begin]
        if end != max_offset:
            test_list[end], test_list[max_offset] = test_list[max_offset], \
                                                    test_list[end]
        begin += 1
        end -= 1
    return test_list


# print(selection_sort(a_list))
print(selection_sort_optimize(a_list))

# END
