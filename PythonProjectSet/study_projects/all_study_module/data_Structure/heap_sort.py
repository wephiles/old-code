# -*- coding: utf-8 -*-
# @CreateTime : 2023/10/26 026 19:30
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/heap_sort.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles


def create_max_heap(array: list[int]):
    """
    构造大根堆
    Returns
    -------

    """
    for i in range(len(array) // 2, 0, -1):
        adjust_heap(array, i)


def adjust_heap(array: list[int], k: int):
    """
    调整堆
    Returns
    -------

    """
    array[0] = array[k]
    i: int = 2 * k
    while i <= len(array):
        if i < len(array) and array[i] < array[i + 1]:
            i += 1
        if array[0] > array[i]:
            break
        else:
            array[k] = array[i]
            k = i
        i *= 2
    array[k] = array[0]


def heap_sort(array: list[int]):
    """
    堆排序
    Returns
    -------

    """
    create_max_heap(array)
    for i in range(len(array), 0, -1):
        array[i], array[1] = array[1], array[i]
        adjust_heap(array, 1)


array = [12, 11, 13, 5, 6, 7]
heap_sort(array)
# END
