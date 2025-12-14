'''
Created on 2020-8-26

@author: 20866
'''

print("****************************************")
#接上，正则表达式
# import re
# import re
# matchobj = re.match(r'[0-9]*', "149489", re.M|re.I)#.(英文句点)匹配除换行符 \n 之外的任何单字符。
# if matchobj:
#     print(matchobj.group())
# else:
#     print("error!!!")
# #运行结果：149489

# import re
# matchobj = re.match(r'<.*?>', "<1>4948<9>", re.M|re.I)#.(英文句点)匹配除换行符 \n 之外的任何单字符。
# if matchobj:
#     print(matchobj.group())
# else:
#     print("error!!!")
# #运行结果：<1> 非贪婪的表达式，匹配最小的单位

# import re
# matchobj = re.match(r'<.*?>', "<149489>", re.M|re.I)#.(英文句点)匹配除换行符 \n 之外的任何单字符。
# if matchobj:
#     print(matchobj.group())
# else:
#     print("error!!!")
# #运行结果：<149489> 非贪婪的表达式，匹配最小的单位

# import re
# matchobj = re.match(r'<.*>', "<1>4948<9><056498>", re.M|re.I)#.(英文句点)匹配除换行符 \n 之外的任何单字符。
# if matchobj:
#     print(matchobj.group())
# else:
#     print("error!!!")
# #运行结果：<1>4948<9><056498> 贪婪的表达式，匹配所有的
# 
# import re
# matchobj = re.match(r'.*', "<1>4948<9><056498>", re.M|re.I)#.(英文句点)匹配除换行符 \n 之外的任何单字符。
# if matchobj:
#     print(matchobj.group())
# else:
#     print("error!!!")
# #运行结果：<1>4948<9><056498>

# import re
# matchobj = re.match(r'<.*>?', "<1>4948<9><198489>", re.M|re.I)#.(英文句点)匹配除换行符 \n 之外的任何单字符。
# if matchobj:
#     print(matchobj.group())
# else:
#     print("error!!!")
# #运行结果：<149489> 非贪婪的表达式，匹配最小的单位

# import re
# matchobj = re.match(r'<\w+?>?', "<1>4948<9><198489>", re.M|re.I)  #   \w 匹配字母或数字或下划线
# if matchobj:
#     print(matchobj.group())
# else:
#     print("error!!!")

# import re 
# line = "chapter"
# matchobj = re.match(r'\bchap',line,re.M|re.I)
# if matchobj:
#     print(matchobj.group())
# else:
#     print("Error!!!")

# import re 
# line = "(fytd)c56489(yrd)trd445(468)"
# match1obj = re.match(r'(.*)?',line,re.M|re.I)
# if match1obj:
#     print(match1obj.group())
# else:
#     print("error!!!")
# #运行结果：(fytd)c56489(yrd)trd445(468)

# import re 
# line = "(fytd)c56489(yrd)trd445(468)"
# match1obj = re.match(r'(.*)',line,re.M|re.I)
# if match1obj:
#     print(match1obj.group())
# else:
#     print("error!!!")
# #运行结果：(fytd)c56489(yrd)trd445(468)

# import re 
# line = "Chapter"
# match1obj = re.match(r'\Bapt',line,re.M|re.I)
# if match1obj:
#     print(match1obj.group())
# else:
#     print("error!!!")
# #运行结果：error!!!

# import re 
# line = "aptitude"
# match1obj = re.match(r'\Bapt',line,re.M|re.I)
# if match1obj:
#     print(match1obj.group())
# else:
#     print("error!!!")
# #运行结果：error!!!

# import re
# print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配
# '''运行结果(0, 3)
#           (11, 14)'''
          
# import re
# print(re.search('www', 'www.runoob.com'))  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com'))
# '''运行结果：<re.Match object; span=(0, 3), match='www'>
# <re.Match object; span=(11, 14), match='com'>
# '''

# import re
# searchobj1 = re.search(r'dogs', "the dogs are amarter than cats.", re.M|re.I)
# if searchobj1:
#     print(searchobj1.group())
# else:
#     print("error!!!")
# matchobj1 = re.match(r'dogs', "the dogs are amarter than cats.", re.M|re.I)
# if matchobj1:
#     print(matchobj1.group())
# else:
#     print("error!!!")
# '''运行结果：dogs
# error!!!
# '''

###  检索和替换,Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。
### 语法：语法：re.sub(pattern, repl, string, count=0, flags=0)
### pattern : 正则中的模式字符串
### repl : 替换的字符串，也可为一个函数。### 注意：repl 参数是一个函数
### string : 要被查找替换的原始字符串。
### count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

# import re
# phone = "2004-656-545 # 这是一个国外的电话号码！"
# # 删除字符串中的 Python注释 
# num = re.sub(r'#.*$',"",phone) #替换 将phone中匹配到r'#.*$'的字符替换为""
# print(num)
# # 删除非数字(-)的字符串 
# num = re.sub(r'\D',"",phone) #替换      \D匹配数字符号，而\d匹配非数字符号
# print(num)
# '''运行结果：
# 2004-656-545 
# 2004656545
# '''
# 
# phone = "2004-656-545 # 这是一个国外的电话号码！"
# # 删除字符串中的 Python注释 
# num = re.sub(r'#.*$',"hello",phone) #替换 将phone中匹配到r'#.*$'的字符替换为""
# print(num)
# # 删除非数字(-)的字符串 
# num = re.sub(r'\D',"yes",phone) #替换      \D匹配数字符号，而\d匹配非数字符号
# print(num)
# '''运行结果：
# 2004-656-545 hello
# 2004yes656yes545yesyesyesyesyesyesyesyesyesyesyesyesyesyesyes
# '''

# def double(matched):
#     value = int(matched.group('value'))
#     return str(value*2)
# s = "A23G4HFD567"
# print(re.sub('(?P<value>\d+)',double,s))
#  
# '''输出结果：
# A46G8HFD1134
# '''
# 
# '''
# re.compile 函数:compile 函数用于编译正则表达式，生成一个
# 正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
# 语法格式为：re.compile(pattern[, flags])
# '''
# 
# pattern = re.compile(r'\d+')                 # 用于匹配至少一个数字
# m =pattern.match('one12twothree34four')  # 查找头部，没有匹配
# print(m)
# m = pattern.match("one12twothree34four",2,10)# 从'e'的位置开始匹配，没有匹配
# print(m)
# m = pattern.match("one12twothree34four",3,10)# 从'1'的位置开始匹配，正好匹配
# print(m)# 返回一个 Match 对象
# print(m.group(0) )
# print(m.start(0))
# print(m.end(0))
# print(m.span(0))
# '''
# group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
# start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
# end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
# span([group]) 方法返回 (start(group), end(group))。
# '''

# pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
# m = pattern.match('Hello World Wide Web1.0')
# print(m)    # 匹配成功，返回一个 Match 对象
# print (m.group(0))    # 返回匹配成功的整个子串                           
# print (m.group(1))      # 返回第一个分组匹配成功的子串
# print (m.span(1))     # 返回第一个分组匹配成功的子串的索引
# print (m.group(2))         # 返回第二个分组匹配成功的子串  
# print (m.span(2))           # 返回第二个分组匹配成功的子串
# print(m.groups())        # 等价于 (m.group(1), m.group(2), ...)
# #print(m.group(3))          # 不存在第三个分组
