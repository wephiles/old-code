# -*- coding: utf-8 -*-
# @CreateTime : 2023/10/26 026 19:00
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/quick_sort.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles


# def quick_sort(arr: list[int]) -> list:
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)


# 下面是划分
def partition(array: list[int], low: int, high: int):
    pivot = array[low]
    while low < high:
        while low < high and array[high] >= pivot:
            high -= 1
        array[low] = array[high]

        while low < high and array[low] <= pivot:
            low += 1
        array[high] = array[low]

    array[low] = pivot
    return low


def quick_sort(array: list[int], low: int, high: int):
    if low < high:
        pivot_position = partition(array, low, high)
        quick_sort(array, low, pivot_position - 1)
        quick_sort(array, pivot_position + 1, high)


arr = [3, 6, 8, 10, 1, 2, 1]
quick_sort(arr, 0, len(arr) - 1)

print(arr)
# END
