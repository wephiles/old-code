'''
Created on 2021-1-2

@author: 20866
'''

# print('C:\py\code.py')
# print(len('C:\py\code.py'))
#
# ###208页
#
# print('spam' in 'aspam')
#
# ### 211页
#
# L = [0,1,2,3,4,5,6,7,8,9,10,11]
# print(L[1:10])
# print(L[1:10:2])
#
# print("hello"[::-1])
#
# ###O'Reilly 奥莱利  213页
#
# ### repr(obj)函数：内置函数 返回一个对象的字符串值
# print(repr(12))
# print(repr("12"))
# print(repr('buweishi'))
# print(repr("buweishi"))
# print(repr([1,2,3]))
# print(   repr(  (1,2,3)  )    )
# print( repr( {1,2,3} )   )
# print( repr( {'a':1,"b":2} )   )
# 12
# '12'
# 'buweishi'
# 'buweishi'
# [1, 2, 3]
# (1, 2, 3)
# {1, 2, 3}
# {'a': 1, 'b': 2}



# S = 'buweishi'
# S1 = list(S)
# print(S1)
# 
# S = ' '.join(S1)
# print(S)
# 
# S = '|'.join(S1)
# print(S)

# S = 'aaa bbb ccc'
# print(S.split())
#  
# S = 'a|bbb|cc'
# print(S.split())
#  
# S = 'aaa|bbb|ccc'
# print(S.split())
#  
# # ['aaa', 'bbb', 'ccc']
# # ['a|bbb|cc']
# # ['aaa|bbb|ccc']

# S = 'aa|bbb|c'
# print(S.split('|'))

# print("hello %r"%'nihqo')
# print("hello %s"%'nihqo')
# hello 'nihqo'
# hello nihqo

# print(repr("buweishi"))
# print(repr('buweishi'))
# print(repr(154))

# 'buweishi'
# 'buweishi'
# 154

# x = 1234
# print(",,%d,,,%-6d,,,%06d,"%(x,x,x))

# import sys
# print("My {1[spam]} runs {0.platform}".format(sys,{'spam':"laptop"}))
# print("My {0[spam]} runs {1.platform}".format({'spam':"laptop"},sys))
# print("my {config[spam]} runs {sys.platform}".format(sys = sys, config={'spam':'laptop'}))
# # My laptop runs win32
# # My laptop runs win32
# # my laptop runs win32
### 列表、字典
# L = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# print(L)
# # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 
# L.append([1,2,3])
# print(L)
# # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3]]
# L1 = L + [[4,5,6]] 
# print(L)
# print(L1)
# # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3]]
# # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6]]
# L1 = L + [4,5,6]
# print(L)
# print(L1)
# # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3]]
# # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], 4, 5, 6]

 
# L = [2,3,1]
# print(L.sort_class())
# # None

# L = [2,3,1]
# L.sort_class()
# print(L)
# # [1, 2, 3]

# L = ['ABd','bBc','dBa','CBb']
# L.sort_class()
# print(L)
# 
# L.sort_class(key=str.lower)
# print(L)
# 
# L = ['abc','ABD','aBe']
# X = sorted([x.lower() for x in L])
# print(X)

# L = [1,2]
# L.append({'a':1,'b':2})
# print(L)
# 
# L.append((1,2,3))
# print(L)
# 
# L.extend([9,10,11])
# print(L)
# 
# L.extend([9])
# print(L)

# L = [1,2,3]
# L.pop()
# print(L)

# ### 用列表pop和append方法实现堆栈结构：
# L = []
# L.append(1) ###进栈
# L.append(2) ###进栈
# L.pop()
# print(L)

# L = [1,2,3,4,5,6,7,8,9]
# print(L.index(5, 3, 8))
# 
# L.insert(1,'buweishi')
# print(L)
# 
# L.remove(8)
# print(L)

# 4
# [1, 'buweishi', 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 'buweishi', 2, 3, 4, 5, 6, 7, 9]

# L = [1,2,3,4,5,6,7,8,9]
# del L[0]
# print(L)

# print(help(dict))
# print(dir(dict))

# D = {'a':1,'b':2,'c':3}
# D.pop('b')
# print(D)

# table = {'python':'guido van Rossum',
#          'perl':'Larry Wall',
#          'Tcl':'John Ousterhout'}
# print(table)
# creator = table['python']
# print(creator)
# 
# for language in table:
#     print(language + '\t' +table[language])
#     
# # {'python': 'guido van Rossum', 'perl': 'Larry Wall', 'Tcl': 'John Ousterhout'}
# # guido van Rossum
# # python    guido van Rossum
# # perl    Larry Wall
# # Tcl    John Ousterhout

# ###建立字典的四种方法：
# ### 第一种：
# print({'a':1,'b':2})
# ### 第二种：
# D = {}
# D['name']='BuWeishi'
# D['number']='250'
# print(D)
# ### 第三种：
# D1 = dict(name='buweishi',number='250')
# print(D1)
# ###第四种：
# D2 = dict([('name','number'),('buweishi','250')])
# print(D2)
# 
# #如果所有键的值都相同，可以使用这种特殊的方式进行初始化！
# D = dict.fromkeys(['a','b'],0)
# print(D)

# L = list(zip(['a','b','c'],[1,2,3]))
# print(L)
# 
# D = dict(zip(['a','b','c'],[1,2,3]))
# print(D)
# # [('a', 1), ('b', 2), ('c', 3)]
# # {'a': 1, 'b': 2, 'c': 3}

# D = {k:v for (k,v) in zip(['a','b','c'],[1,2,3])}
# print(D)



### 262页
### file:///F:/python/Python%E5%AD%A6%E4%B9%A0%E6%89%8B%E5%86%8C(%E7%AC%AC4%E7%89%88).pdf

# L = [1,2,3,4,5,6]
# del L[0:len(L)]
# print(L)
# for i in range(1,1):
#     print(i)

# print("a")






























































































































































































































































