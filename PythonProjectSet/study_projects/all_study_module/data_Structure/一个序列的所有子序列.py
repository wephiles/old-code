# -*- coding: utf-8 -*-
# @CreateTime : 2023/11/8 008 17:19
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/一个序列的所有子序列.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles

def print_subsequences(arr):
    """
    { }
    { 1 }
    { 2 }
    { 1 2 }
    { 3 }
    { 1 3 }
    { 2 3 }
    { 1 2 3 }

    求一个序列的所有子序列

    Parameters
    ----------
    arr

    Returns
    -------

    """
    n = len(arr)
    total = 1 << n  # 左移 n 位 高位丢弃 低位补0
    for i in range(total):  # 恰好是从 00000 - 11111（0 - 31） 注意： 1 << 5 = 32
        print('{', end=' ')
        for j in range(n):
            if i & (1 << j):  # & 按位与
                print(arr[j], end=" ")
        print('}', end=' ')
        print()


arr = [1, 2, 3]
print_subsequences(arr)

# END
