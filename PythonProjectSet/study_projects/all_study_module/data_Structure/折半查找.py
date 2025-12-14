# -*- coding: utf-8 -*-
# @CreateTime : 2023/8/27 027 22:57
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/折半查找.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles


def binary_search(nums: list[int], num: int):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if num > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if low < len(nums) and nums[low] == num:
        return low
    return -1


print(binary_search([1, 2, 3, 10, 25, 26, 30, 58, 69, 100], 1000))
# END
