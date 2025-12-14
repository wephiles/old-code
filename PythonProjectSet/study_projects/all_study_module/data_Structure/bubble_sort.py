# -*- coding: utf-8 -*-
# @CreateTime : 2023/7/16 016 20:24
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/bubble_sort.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles

a_list = [98, 94, 2, -12, 4, 19, 50, 48, -100, -10]


# a_list = [48, 50, 19, 4, 2, 94, 98]


# 普通冒泡排序
def bubble_sort(sort_list: [int]) -> list[int]:
    """

    Parameters
    ----------
    sort_list
    A list which need to be sorted.
    Returns
    -------
    A list which has been sorted.
    """
    if len(sort_list) == 0:
        return []
    length = len(sort_list)
    for i in range(0, len(sort_list)):
        for j in range(0, len(sort_list) - 1):
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
    return sort_list


# # 冒泡排序的优化
# def bubble_sort_optimize(sort_list: [int]) -> list[int]:
#     """
#
#     Parameters
#     ----------
#     sort_list
#
#     Returns
#     -------
#
#     """
#     # flag 标识有无交换，值为true表示有交换，为false标识没有交换
#
#     exchange = 0
#     if len(sort_list) == 0:
#         return []
#     for i in range(0, len(sort_list)):
#         flag = False
#         for j in range(0, len(sort_list) - 1):
#             exchange += 1
#             if sort_list[j] > sort_list[j + 1]:
#                 flag = True
#                 sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
#         if not flag:
#             print(exchange)
#             return sort_list
#     print(exchange)
#     return sort_list
#
#
# # 倒序冒泡排序
# def bubble_sort_reverse_order(sort_list: [int]):
#     """
#
#     Parameters
#     ----------
#     sort_list
#
#     Returns
#     -------
#
#     """
#     exchange = 0
#     if len(sort_list) == 0:
#         return []
#     for i in range(len(sort_list) - 1, -1, -1):
#         for j in range(len(sort_list) - 1, 0, -1):
#             exchange += 1
#             if sort_list[j] < sort_list[j - 1]:
#                 sort_list[j], sort_list[j - 1] = sort_list[j - 1], sort_list[j]
#     print(exchange)
#     return sort_list
#
#
# # 倒序冒泡排序 优化
# def bubble_sort_reverse_order_optimize(sort_list: [int]):
#     """
#
#     Parameters
#     ----------
#     sort_list
#
#     Returns
#     -------
#
#     """
#     exchange = 0
#     if len(sort_list) == 0:
#         return []
#     for i in range(len(sort_list) - 1, -1, -1):
#         flag = False
#         for j in range(len(sort_list) - 1, 0, -1):
#             exchange += 1
#             if sort_list[j] < sort_list[j - 1]:
#                 sort_list[j], sort_list[j - 1] = sort_list[j - 1], sort_list[j]
#                 flag = True
#         if not flag:
#             print(exchange)
#             return sort_list
#     print(exchange)
#     return sort_list
#
#
# # 冒泡排序优化—更进一步
# def bubble_sort_optimize_boundary(sort_list: [int]) -> list[int]:
#     """
#
#     Parameters
#     ----------
#     sort_list
#
#     Returns
#     -------
#
#     """
#
#     '''
#     冒泡排序第二次优化：
#     添加一个边界值，比到边界值的时候就停止，不用再比较
#     '''
#     last_swap_index: int = 0  # 最后一次交换的下标
#     list_boundary = len(sort_list) - 1  # 无序列表的边界， 每次比较到这个地方就停止比较
#     exchange = 0
#     for i in range(0, len(sort_list) - 1):
#         flag: bool = False
#         for j in range(0, list_boundary):
#             exchange += 1
#             if sort_list[j] > sort_list[j + 1]:
#                 sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
#                 flag = True
#                 last_swap_index = j
#         list_boundary = last_swap_index
#         if not flag:
#             print(exchange)
#             return sort_list
#     print(exchange)
#     return sort_list

print(bubble_sort(a_list))  # 对于[48, 50, 19, 4, 2, 94, 98] 交换次数 42
# print(bubble_sort_optimize(a_list))  # 对于[48, 50, 19, 4, 2, 94, 98] 交换次数30
# print(bubble_sort_reverse_order(a_list))
# print(bubble_sort_reverse_order_optimize(a_list))
# print(bubble_sort_optimize_boundary(a_list))  # 对于[48, 50, 19, 4, 2, 94, 98]
# 交换次数12

# TODO: 还可以针对内存进行优化，即在交换的地方可以使用异或进行优化

# END
