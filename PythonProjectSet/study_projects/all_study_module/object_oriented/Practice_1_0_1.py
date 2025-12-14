'''
Created on 2020-8-26

@author: 20866
'''

#错误和异常
# print("-------------------------")
# while True:
#     try:#可能出现异常的代码放在try语句块里面
#         x=int(input("please input a number:"))
#         print(x)
#         break
#     except ValueError:#如果有异常，就用关键字except（除了，处...之外）处理这个异常
#         print("not volid input , try again! ")


# for i in range(1,10):
#     try:
#         x = int(input("Please enter a number : "))
#         #break
#     except:
#         print("Not the number ! Please enter a number.")
#     else:
#         print(x)

# 用raise 触发异常
# y = 6
# if y > 5:
#     raise Exception('y 不能大于 5。y 的值为: {}'.format(y))#Exception是一个类

# import requests
# r=requests.get("http://www.baidu.com")
# r.status_code
# r.encoding = "utf-8"    
# r.text
'''  正则表达式: '''

'''re.match方法： 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。'''


# import re
# print(re.match('www', 'www.runoob.com'))
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# 
# print(re.match('www.r', 'www.runoob.com').span())
# print(re.match('www.r', 'www.runoob.com'))
# 
# print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

# import re
# line = "Cats are smarter than dogs"
# '''re.match(pattern, string, flags=0)'''
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
# # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# if matchObj:
#     print ("matchObj.group() : ", matchObj.group())
#'''
#group(num=0)    匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
#'''
#     print ("matchObj.group(1) : ", matchObj.group(1))
#'''
#groups()    返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
#'''
#     print ("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print ("No match!!")


""" re.search方法: """
"""re.search 扫描整个字符串并返回第一个成功的匹配。 函数语法： re.search(pattern, string, flags=0)"""

# import re
# print(re.search(r'www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.search(r'com', 'www.runoob.com').span())  # 不在起始位置匹配
# print(re.search(r'www', 'wwwrunoobcom').span())
# print(re.search(r'com', 'wwwrunoobcom').span())
# 
# print("-------------")
# 
# print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配
# print(re.search('www', 'wwwrunoobcom').span())
# print(re.search('com', 'wwwrunoobcom').span())
# 
# print("-------------")
# import re
#   
# line = "Cats are smarter than dogs"
#   
# searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
#   
# if searchObj:
#     print ("searchObj.group() : ", searchObj.group())
#     '''
#         group(num=0)    匹配的整个表达式的字符串，group() 可以一次输入多个组号，
#             在这种情况下它将返回一个包含那些组所对应值的元组。
#     '''
#     print ("searchObj.group(1) : ", searchObj.group(1))
#     '''
#         groups()    返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
#     '''
#     print ("searchObj.group(2) : ", searchObj.group(2))
# else:
#     print ("Nothing found!!")


# # re.match与re.search的区别:
# # re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，
# # 而 re.search 匹配整个字符串，直到找到一个匹配。

# import re
#  
# line = "Cats are smarter than dogs"
#  
# matchObj = re.match( r'dogs', line, re.M|re.I)
# if matchObj:
#     print ("match --> matchObj.group() : ", matchObj.group())
# else:
#     print ("No match!!")
#  
# matchObj = re.search( r'dogs', line, re.M|re.I)
# if matchObj:
#     print ("search --> matchObj.group() : ", matchObj.group())
# else:
#     print ("No match!!")

#
# #检索和替换：
# # Python 的re模块提供了re.sub用于替换字符串中的匹配项
# # 语法：
# # re.sub(pattern, repl, string, count=0, flags=0)
# # 参数：
# # pattern : 正则中的模式字符串。
# # repl : 替换的字符串，也可为一个函数。
# # string : 要被查找替换的原始字符串。
# # count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
# # flags : 编译时用的匹配模式，数字形式。
# # 前三个为必选参数，后两个为可选参数。
# import re

# phone = "2004-959-559 # 这是一个电话号码"

# # 删除注释
# num = re.sub(r'#.*$', "", phone)
# print ("电话号码 : ", num)
#  
# # 移除非数字的内容
# num = re.sub(r'\D', "", phone)
# print ("电话号码 : ", num)

# import re
# matchobj = re.match(r'runoo+b', "runoob", re.M|re.I)
# if matchobj:
#     print(matchobj.group())
# else:
#     print("error!!!")

# import re
# matchobj = re.match(r'runoo+b', "runoobrunooooob", re.M|re.I)
# if matchobj:
#     print(matchobj.group())
# else:
#     print("error!!!")

# import re
# matchobj = re.match(r'runoo*b', "runooooob", re.M|re.I)
# if matchobj:
#     print(matchobj.group())
# else:
#     print("error!!!")

# import re
# matchobj = re.match(r'runoo?b', "runooooob", re.M|re.I)
# if matchobj:
#     print(matchobj.group())
# else:
#     print("error!!!")

# import re
# matchobj = re.match(r'[0-9]{1,2}', "12", re.M|re.I)
# if matchobj:
#     print(matchobj.group())
# else:
#     print("error!!!")

# import re
# matchobj = re.match(r'[1-9][0-9]?', "3452", re.M|re.I)
# if matchobj:
#     print(matchobj.group())
# else:
#     print("error!!!")

# import re
# matchobj = re.match(r'[1-9][0-9]{0,1}', "345", re.M|re.I)
# if matchobj:
#     print(matchobj.group())
# else:
#     print("error!!!")

# import re
# matchobj = re.match(r'<\w+?>', "<h1>RUNOOB-菜鸟教程</h1>", re.M|re.I)#.(英文句点)匹配除换行符 \n 之外的任何单字符。
# if matchobj:
#     print(matchobj.group())
# else:
#     print("error!!!")

# import re
# matchobj = re.match(r'[0-9]*', "149489", re.M|re.I)#.(英文句点)匹配除换行符 \n 之外的任何单字符。
# if matchobj:
#     print(matchobj.group())
# else:
#     print("error!!!")

# import re
# matchobj = re.match(r'[0-9]*', "149489", re.M|re.I)#.(英文句点)匹配除换行符 \n 之外的任何单字符。
# if matchobj:
#     print(matchobj.group())
# else:
#     print("error!!!")
