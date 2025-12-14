# -*- codeing = utf-8 -*-
# @Time : 2021/6/1 14:05
# @Auther : 20866
# @Site : 
# @File : Test_Bs4.py
# @Software : PyCharm
import re

from bs4 import BeautifulSoup
### beautifulsoup:将复杂的HTML文档转换成一个复杂的树形结构 每个节点都是python对象 所有对象都可以归纳为四种：

'''
- Tag
- NavigableString
- BeautifulSoup
- Comment
'''


file = open("./百度网页.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")

### 1.- Tag (标签及其内容 只能拿到第一个符合的内容)

# print(bs.title)
### <title>百度一下，你就知道</title>
# print(bs.a)
### <a class="toindex" href="/">百度首页</a>

'''  查找第一个符合条件的HTML文档的内容（标签）'''
# print(type(bs.title))
# print(type(bs.a))
# print(type(bs.head))

'''
<class 'bs4.element.Tag'>
<class 'bs4.element.Tag'>
<class 'bs4.element.Tag'>
'''

### 2.- NavigableString 标签里的内容（字符串）

# print(bs.title.string)
# print(bs.a.string)
'''
百度一下，你就知道
百度首页
'''
# print(type(bs.title.string))
# print(type(bs.a.string))

'''
<class 'bs4.element.NavigableString'>
<class 'bs4.element.NavigableString'>
'''

### 3. BeautifulSoup

# print(bs.a.attrs)
### {'class': ['toindex'], 'href': '/'}
# print(type(bs))
# ### <class 'bs4.BeautifulSoup'> 表示整个文档
# print(bs.name)
# ### [document]
# print(bs.attrs)
# ### {}
# print(bs)
### 4. comment 是一个特殊的NavigableString ( 有注释的文字的类型 ) 输出的内容不包括注释符号
#
### --------------------------------------------------------------------------

###文档的遍历

# print(bs.head.contents) ###返回一个列表

# print(bs.head.contents[1])

###更多内容 搜索beautifulsoup文档
### 文档的搜素
### 1. find_all 字符串过滤 查找与字符串完全匹配的内容
# t_list = bs.find_all('a')
# print(t_list)


### 2. 正则表达式方式搜索  使用search()方法匹配内容
t_list = bs.find_all(re.compile("a")) ### 所有包含"a"的内容  匹配
print(t_list)











































































































