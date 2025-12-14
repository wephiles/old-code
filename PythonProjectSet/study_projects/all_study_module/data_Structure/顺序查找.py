# -*- coding: utf-8 -*-
# @CreateTime : 2023/8/27 027 22:54
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/顺序查找.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles


# def search(nums: list[int], elem: int):
#     if elem in nums:
#         return nums.index(elem)
#     return -1
#
#
# print(search([1, 2, 3, 45, 30, 10], 100))

def print_all_subset(a: list[int]):
    # t = 1 << len(a)
    for i in range(0, len(a)):
        j = 1
        k = 0
        print('{')
        while j:
            if j & i:
                print(a[j])
                j >> i
                k += 1
        print('}')


print_all_subset([1, 2, 3, 4, 5, 6])

# ENDl
