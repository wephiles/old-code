'''
Created on 2020-12-29

@author: 20866
'''


# import decimal
# from fractions import Fraction

# print("--------------------------------------------")
# print(2%3)#取余
# print(2/3)#真正除法
# print(2//3)#取整
# x,y,z = 2,4,6
# if x<y<z:
#     print("yes")
#
# if x<y and y<z:
#     print("yes")
#
# if x<y & y<z:
#     print("yes")
#
# print(1j*1J)
#
# x = 1
# y = 1
#
# print("x<<2={0}".format(x<<2))
#
# print("y>>2={0}".format(y>>2))
#
# print(bin(60))       #0b111100
# print(bin(60<<3))    #0b111100000 左移
# print(bin(60>>3))    #0b111     右移
#
#
# x = 1
# y = 0
# if x & y :
#     print("yes")
# else:
#     print("no")
# import math
# print(math.sqrt(2))
# print(math.sqrt(3))
# print(math.sqrt(5))
# print(math.sqrt(7))
# print(math.e)
#
# 根号二 ：1.414
# 根号三 ：1.732
# 根号五 ：2.236
# 根号七 ：2.646
# 自然对数底数e ：2.71828

#171页

# import math
# print(math.sqrt(144))
# print(144**(1/2))
# print(math.pow(144,1/2))
# print(0.1+0.1+0.1-0.3)
# #5.551115123125783e-17
# from decimal import Decimal
#
# X = Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')
# print(X)
# #0.0
#
# X = Decimal(0.1)+Decimal(0.1)+Decimal(0.1)-Decimal(0.3)
# print(X)
# #2.775557561565156540423631668E-17
#
#
# X = 0.1 +0.1 +0.1 - 0.3
# print(X)
# #5.551115123125783e-17
# #设置全局精度
#
# x = decimal.Decimal(1)/decimal.Decimal(7)
# print(x)
# x = 1 / 7
# print(x)
# 0.1428571428571428571428571429
# 0.14285714285714285

###指定精度：
# decimal.getcontext().prec = 4
# x = decimal.Decimal(1)/decimal.Decimal(7)
# print(x)
# #0.1429
#
#
# x = 1234 + 0.33
# print(x)
# ##1234.33
#
# x = 1999 + 1.33
# print(x)

#174页

# x = Fraction(1,3)
# y = Fraction(4,6)
# print(x,y)
### 1/3 2/3

# print(Fraction(1,2),Fraction(1,3),Fraction(3,3),Fraction(2,1),Fraction(2,6))
### 1/2 1/3 1 2 1/3

# x = Fraction("0.25")
# print(x)
# # 1/4
# 
# y = Fraction("1.25")
# print(y)
# # 5/4
# 
# print(Fraction("0.25")+Fraction("1.25"))
# # 3/2
# 
# print(x + y)
# # 3/2
#
# a = 1 / 3.0
# b = 4 / 6.0
# print(a)
# print(b)
# print(a+b)
# print(a-b)
# print(a*b)
# 0.3333333333333333
# 0.6666666666666666
# 1.0
# -0.3333333333333333
# 0.2222222222222222
### 175页
# x = decimal.Decimal(str(1/3))+decimal.Decimal(str(2/3))
# print(x)
# x = 1/3 + 2/3
# print(x)

# 0.9999999999999999
# # 1.0
#
# print(1000.0/1234567890)
# print(1000/1234567890)
# print(Fraction(1000,123456789000))
# 8.100000073710001e-07
# 8.100000073710001e-07
# 1/123456789

###集合 唯一的 不可变的对象的无序组合  
###集合里面不能包含list列表 dict字典  但是能包含元组 数字 字符串  
###集合是可迭代的

# x = set('abcde')
# print(x)
# x = {'a',2.5,6,'b',(5,4,3,2,1)}
# print(x)
#
# x = {(1,2,3,4,5)}
# print(x)
#
# x = set("abcdefghijklmnopqrstuvwxyz")
# y = set("buweishi")
# print( x | y )
# print( x & y )
# print( x - y )
# print( x ^ y ) ###两个集合中不同的元素！！！
#
#
# x = (1,2,3)
# for i in x:
#     print(i*2)
#
# x = set([1,2,3,4])
# print(x)
# x = set({1,2,3,4})
# print(x)
#
# x = {1,2,3,4,'bt','a'}
# print(x)
#
# x = set((1,2,3,4))
# print(x)
#
# for x in [1,2,3,5]:
#     print({x})
#
#
# for x in {1,2,3,4}:
#     print(x)
#
# x = set([1,2,3,4])
# y = set((1,2,3,4))
# print(x,y)
# print(type(True))
# print(isinstance(True,int))
# print(True == 1)
# print(True is 1)
# print(True or False)
# print(True + 4)
# <class 'bool'>
# True
# True
# False
# True
# 5

# l1 = [2,3,4]
# l2 = l1
# print(l1,l2)
# ###[2, 3, 4] [2, 3, 4]
# l1[0] = 10
# print(l1,l2)
# 
# ###[10, 3, 4] [10, 3, 4]

# l1 = [2,3,4]
# l2 = l1[:]
# print(l1,l2)
# ###[2, 3, 4] [2, 3, 4]
# 
# l1[0] = 10
# print(l1,l2)
# ###[10, 3, 4] [2, 3, 4]

# import sys
# # print(sys.getrefcount(1))
#
# print("C:\new\text.spm")
# # C:
# # ew    ext.spm
#
# print(r"C:\new\text.spm")
# ###C:\new\text.spm
#
# print("C:\\new\\text.spm")
# ###C:\new\text.spm
