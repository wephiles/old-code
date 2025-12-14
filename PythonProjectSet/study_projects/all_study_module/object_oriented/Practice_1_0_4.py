'''
Created on 2020-8-26

@author: 20866
'''
# from builtins import set
# '''
# print("---------------------------------------------")
# #print(3.1415*2)
# #math模块
# import math 
# print(math.pi)
# print(math.sqrt(25))
# #产生随机数
# import random
# print(random.random())
# print(random.choice([0,1,2,3,4,5,6,7,8,9])  )  
# '''
# '''
# import mysql.connector                 
# 
# # mysql1.py
# config = {
#     'host': '127.0.0.1',
#     'user': 'root',
#     'password': 'root',
#     'port': 3306,
#     'database': 'test',
#     'charset': 'utf8'
# }
# try:
#     cnn = mysql.connector.connect(**config)
# except mysql.connector.Error as e:
#     print("hello-------------------------")
#     print('connect fails!{}'.format(e) )
# cursor = cnn.cursor()
# try:
#     sql_query = 'select name,age from stu ;'
#     cursor.execute(sql_query)
#     for name, age in cursor:
#         print (name, age)
# except mysql.connector.Error as e:
#     print('query error!{}'.format(e))
# finally:
#     cursor.close()
#     cnn.close()
# '''
# #128页    
# L='hello'
# S='world'
# C='python'
# List=[L,S,C]
# # print(List.pop(0))
# # print(List)
# del List[1]
# print(List)
# List.append('libai')
# print(List)
# #133页
# M=[[1,2,3],[4,5,6],[7,8,9]]
# col2=[row[2] for row in M]
# print(col2)
# 
# col1=[row[0]+1 for row in M]
# print(col1)
# 
# col3=[row[0] for row in M if row[2]%2==0]
# print(col3)
# 
# for row in M:
#     print(row[0],end=' ')
#     print(row[1],end=' ')
#     print(row[2],end=' ')
# print()
# diag=[M[i][i] for i in [0,1,2]]
# print(diag)
# #138页
# D = {'a':1,'b':2,'c':3,'d':4}
# print('b' in D )
# print('f' in D )
# if not "f" in D:
#     print("not in them!!!") 
# f = open("data.txt",'w')
# f.write('''hello
# thank you
# thank you very much!\n''')
# f.write("你好，谢谢你，非常感谢！\n")
# f.write("你好，谢谢你，非常感谢！\n")
# 
# 
# f = open("data.txt",'r')
# text = f.read()
# print(text)
# f.close()
# 
# #集合
# X = set('buweishi')
# Y = {'w','s','n','b'}#集合像是一个没有值得字典的键
# print(X,Y)
# print(X & Y)
# print(X | Y)
# print(X-Y)
# print(x**2 for x in [1,2,3,4])
# y = ' buweishi'
# print(y*2)
# 
# T = type(X)
# print(T)
# print(type(T))
 
# if type(X) == type([]):
#     print('yes')
# else:
#     print("no")
# if type(X) == set:
#     print('yes')
# if isinstance(L,set):
#     print('yes')
