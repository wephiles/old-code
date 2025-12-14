# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/30 030 8:49
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/quick_sort.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# def partition(data_list: list[int], low: int, high: int) -> int:
#     pivot = data_list[low]
#     while low < high:
#         while low < high and data_list[high] >= pivot:
#             high -= 1
#         data_list[low] = data_list[high]
#         while low < high and data_list[low] <= pivot:
#             low += 1
#         data_list[high] = data_list[low]
#     data_list[low] = pivot
#     return low
#
#
# def quick_sort(data_list: list[int], low: int, high: int):
#     if low < high:
#         pivot_pos = partition(data_list, low, high)
#         partition(data_list, low, pivot_pos - 1)
#         partition(data_list, pivot_pos + 1, high)
#
#
# data_list = [12, -1, 3, 16, 8, 9, 5, 4, -9]
# quick_sort(data_list, 0, len(data_list) - 1)
# print(data_list)


def partition(data: list, low: int, high: int) -> int:
    """
    快速排序的一趟划分，以第一个元素为枢轴。
    Args:
        data (list): 需要划分的数组。
        low (int): 子数组的起始索引。
        high (int): 子数组的结束索引。

    Returns:
        pivot_index (int): 基准元素的索引位置。
    """
    pivot = data[low]
    left = low + 1
    right = high

    while left <= right:
        while left <= right and data[left] <= pivot:
            left += 1
        while left <= right and data[right] >= pivot:
            right -= 1
        if left < right:
            data[left], data[right] = data[right], data[left]

    # 将基准元素放到正确的位置
    data[low], data[right] = data[right], data[low]
    return right


def quick_sort(data: list, low: int, high: int):
    """
    快速排序函数入口，从这里开始递归。
    Args:
        data (list): 需要排序的数组。
        low (int): 子数组的起始索引。
        high (int): 子数组的结束索引。

    Returns:
        None
    """
    if low < high:
        pivot_index = partition(data, low, high)
        quick_sort(data, low, pivot_index - 1)  # 递归排序左侧子数组
        quick_sort(data, pivot_index + 1, high)  # 递归排序右侧子数组


data_list = [2, -1, 3, 4, 6, 5, -1, 9, 10, 47, -9, 11]
quick_sort(data_list, 0, len(data_list) - 1)
print(data_list)

# --END--
