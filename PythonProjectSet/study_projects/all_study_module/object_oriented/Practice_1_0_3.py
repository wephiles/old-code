'''
Created on 2020-8-26

@author: 20866
'''

# print("****************************************")
#接上，正则表达式
# import re
findall:
#
#
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个###列表###，
# 如果没有找到匹配的，则返回空列表。
# 注意： match 和 search 是匹配一次 。 findall 匹配所有。
# 语法格式为：findall(string[, pos[, endpos]])
#
# string : 待匹配的字符串。
# pos : 可选参数，指定字符串的起始位置，默认为 0。
# endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度。


###例:
# pattern = re.compile(r'\d+')
# result1 = pattern.findall('cdnun15619vfe5v1evf1d561v1vfndij61v6')
# result2 = pattern.findall('cdnun15619vfe5v1evf1d561v1vfndij61v6',0,13)
# result3 = pattern.findall('cdnun15619vfe5v1evf1d561v1vfndij61v6',0,7)
# print(result1)
# print(result2)
# print(result3)

# 运行结果：
# ['15619', '5', '1', '1', '561', '1', '61', '6']
# ['15619']
# ['15']

# re.finditer :
# 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，
# 并把它们作为一个迭代器返回。
# re.finditer(pattern, string, flags=0)
# pattern :   匹配的正则表达式
# string :   要匹配的字符串。
# flags :   标志位，用于控制正则表达式的匹配方式，

###例：
# it = re.finditer(r"\d+", "cdnun15619vfe5v1evf1d561v1vfndij61v6")
# # for match in it:
# #     print(match.group())
# 运行结果：
# 561
# 1
# 61
# 6

# 
# re.split  split 方法按照能够匹配的子串将字符串分割后返回列表，
# 它的使用形式如下： re.split(pattern, string[, maxsplit=0, flags=0])
# pattern    匹配的正则表达式
# string    要匹配的字符串。
# maxsplit    分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
# flags    标志位，用于控制正则表达式的匹配方式

# print(re.split('\W+', "python python python"))
# print(re.split('(\W+)', "python python python"))
# print(re.split('\W+', "python python python",1))
# print(re.split('a*', 'hello world'))#对于一个找不到匹配的字符串而言，split 不会对其作出分割

# x = re.search(r"\d*","WW15W.BAI122DUd.C003OM",re.M)
# if x:
#     print(x.group())
# else:
#     print('NONE')
# Python CGI 编程   
# 
# print ("Content-type:text/html")
# print ()                             # 空行，告诉服务器结束头部
# print ('<html>')
# print ('<head>')
# print ('<meta charset="utf-8">')
# print ('<title>Hello Word - 我的第一个 CGI 程序！</title>')
# print ('</head>')
# print ('<body>')
# print ('<h2>Hello Word! 我是来自菜鸟教程的第一CGI程序</h2>')
# print ('</body>')
# print ('</html>')
