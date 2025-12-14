'''
Created on 2020-8-26

@author: 20866
'''
#注释快捷键：ctrl + ( ？/ )键
#面向对象

# print("------------------------")
# #self代表类的实例，并不是类，self并不是Python的关键字.
# #self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self。


# class Myfirstclass:
#     name = ''
#     age = 0
#     __weight = 0
#     def __init__(self,n,a,w):
#         self.name=n
#         self.age=a
#         self.__weight=w
#         print("Are you ready?")
#     def speak(self):
#         print(self.name+" 说："+"我的名字是："+self.name+" , 我"+str(self.age)+'岁了。')
#
#
#
# class Mysecondclass(Myfirstclass):
#     grade=0
#     def __init__(self,n,a,w,g):
#         self.grade=g
#         Myfirstclass.__init__(self,n,a,w)
#
#     def speak(self):
#         print(self.name+" 说："+"我的名字是："+self.name+" , 我"+str(self.age)+'岁了。我现在读 '+str(self.grade)+"年级！")
#
# class Mythirdclass():
#     topic=''
#     name=''
#     def __init__(self,n,t):
#         self.topic= t
#         self.name = n
#         def speak(self):
#             print("my toiic is :"+ self.topice)
#
# class much(Mythirdclass,Mysecondclass):
#     a = ''
#     def __init__(self,n,a,w,g,t):
#         Mysecondclass.__init__(self, n, a, w, g)
#         Mythirdclass.__init__(self, n, t)
#
# allhah = much("buweishi",10,120,1,"Python")
# allhah.speak()
#
# #方法重写:如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法.
# class parent:
#     def myMethod(self):
#         print("父类函数！")
# class child(parent):
#     def myMethod(self):
#         print("调用子类函数！")
# x=parent()
# x.myMethod()
# y=child()
# y.myMethod()
# #类不重写 __init__，实例化子类时，会自动调用父类定义的 __init__。
#
# '''requests 库的get方法'''
# import requests
# r=requests.get("http://www.baidu.com")
# r.status_code
# r.encoding = "utf-8"
# r.text
# import os
# s= os.getcwd()# 返回当前的工作目录
# print(s)
#
# #python正则表达式
# #正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。
# #re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
# import re
# print(re.match('www', 'www.baidu.com').span())
# print(re.match('www', 'www.baidu.com'))
# print(re.match('com', 'www.baidu.com'))
# print(re.match('wwa', 'www.baidu.com'))
#
# line = "Cats are smarter than dogs"
# # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# import re
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
#
# if matchObj:
#     print ("matchObj.group() : ", matchObj.group())
#     print ("matchObj.group(1) : ", matchObj.group(1))
#     print ("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print ("No match!!")
#
# def fun(one,*two,**three):
#     print("one:"+str(one))
#     print("two:"+str(two))
#     print("two:"+str(three))
# fun("nihao!",5,2,3,5,4,name="buweishi",number='1930090102',height='178')
# 字典的遍历（for 循环）
# a_dict={'a':111,'b':222,'c':333}
# for ele in a_dict:
#     print(ele,end=':')
#     print(a_dict[ele])
# #或者：
# for key,elem in a_dict.items():
#     print(key,elem)

# a_string='''I love you 
# you love me
# we are family.
# 
# f = open('C:\\Users\\20866\\Desktop\\我的.txt','w')
# f.write(a_string)
# f.close
# i = 3.21
# print(isinstance(i,int))
# if type(i) == float:
#     print('yes')
# print(round(2.678,2))

# print(int(3.999999999999999))
# # 3
# print(int(3.9999999999999999))
# #4

# e = 5.236
# e = str(e)
# for i in range(-1,-len(e),-1):
#     if e[i] == '.' :
#         print(abs(i+1))
# print(oct(325))

# a = 'A'
# print(a)
# 
# print(bin(23))#### 二进制 
# 
# print(oct(23))#### 八进制
# 
# print(hex(358))#### 十六进制
# 
# print(10**-1)
# class study():
#     time = 10
#     _grade = 0
#     __place = 0
#     def end(self):
#         self.time += 60
#         self._grade += 0.5
#         self.__place += 0.5
# X = study()
# X.end()
# print(X.time)
# # 70
# study().end()
# print(study().time)
# # 10
# print(X._grade)
# # 0.5
# print(X.__place)
# Traceback (most recent call last):
#   File "D:\eclipse_WorkSpace\My_Practice\Practice_1_0_0.py", line 175, in <module>
#     print(X.__place)
# AttributeError: 'study' object has no attribute '__place'
