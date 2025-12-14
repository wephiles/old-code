# -*- coding: utf-8 -*-
# @CreateTime : 2023/11/8 008 22:05
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/求两个等长数组的中位数.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles

def m_search(a: list[int], b: list[int]):
    """
    2011年408数据结构试题：
    -个长度为L(L=1)的升序序列S,处在第[L/2]个位置的数称为S的中位数。例如，若序列S1= (11，13，15,17，19)，则S1的中位
    数是15，两个序列的中位数是含它们所有元素的升序序列的中位数。例如，若S2= (2,.6.8.20)，则S1和S2的中位数为11.。现在有两
    个等长升序序列A和B，试设计一个在时间和空间两方面都尽可能高效的算法，找出两个序列A和B的中位数。要求:

    Parameters
    ----------
    a: list
    b: list

    Returns
    -------

    """
    i: int = 0
    j: int = 0
    if len(a) != len(b):
        print('长度不相等！！！')
        return False
    k = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            k += 1
            if k == len(a):
                return a[i]
            i += 1
        if a[i] > b[j]:
            k += 1
            if k == len(a):
                return b[j]
            j += 1


test_list_11 = [1, 2, 3, 4]
test_list_12 = [1, 2, 3, 4]

test_list_21 = [11, 13, 15, 17, 19]
test_list_22 = [2, 4, 6, 8, 20]

test_list_31 = [2, 3]
test_list_32 = [1, 2]

test_list_41 = [1, 2, 3, 4, 10]
test_list_42 = [1, 2, 3, 4]

print(m_search(test_list_11, test_list_12))
print(m_search(test_list_21, test_list_22))
print(m_search(test_list_31, test_list_32))
print(m_search(test_list_41, test_list_42))

# END
