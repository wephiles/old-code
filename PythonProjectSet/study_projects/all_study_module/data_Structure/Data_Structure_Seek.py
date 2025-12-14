'''
Created on 2021年2月6日

@author: 20866
'''
""" 1.静态查找表 """ 

""" 1.1 顺序查找表 """   
# def SQ_Search(e,L):
#     for i in range(0,len(L)):
#         if e == L[i]:
#             return i+1
#     return 0
# 
# L = [2,5,7,8,9,1,3,6,4]
# print(SQ_Search(3,L))

""" 1.2 有序表查找 """
### 折半查找
# def Binary_Search(e,L):
#     L.sort_class()
#     Lower = 0
#     Higher = len(L) - 1 
#     Count = 0 
#     while Lower <= Higher:
#         Mid = (Lower + Higher) // 2
#         if e == L[Mid] :
#             Count += 1
#             break 
#         elif e < L[Mid]:
#             Higher = Mid - 1
#             Count += 1
#         else:
#             Lower = Mid + 1
#             Count += 1
#     print('查找次数：'+str(Count))
#     if e == L[Mid]:
#         return Mid
#     else:
#         return None
# L = [2,3,5,0,1,8,4,9,10]  
# e = int(input('请输入想要查询的数：'))
# print(Binary_Search(e,L))                

"""2.内部排序："""
"""2.1 直接插入排序 """
def Straight_Insertion_Sort(L):
    L.sort()
    print('系统排序结果：' + str(L))
    L.append(0)# 最后一位当做哨兵
    for i in range(1,len(L)-1):
        L[len(L)-1] = L[i] #将要插入的值赋值给哨兵
        
        
        
    
        
"""277页"""



















