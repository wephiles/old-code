# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/4 22:21
# @Author : 20866
# @Site : 
# @Project: Learn_File
# @File : Regular_Expression.py
# @Software : PyCharm

import re


# re.match(pattern, string, flags=0)
def main():
    a_string = 'Cats are smarter than dogs'
    # a_string = 'None!!@#^&*()&123 hello what 你好啊 niubility!???...>>><<<'
    # result_0 = re.match('[^a-z]+', a_string)
    # print(result_0)
    # <re.Match object; span=(0, 14), match='!!@#^&*()&123 '>
    # result_1 = re.match(r'[^a-z]+', a_string)
    # print(result_1)
    # result_2 = re.match('.*', a_string)
    # print(result_2)

    # re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

    # a_string = 'Cats are smarter than dogs'
    # result = re.match(r'(.*)are(.*?).*', a_string)
    # print(result.group())
    # print(result.group(1))
    # print(result.group(2))
    # re.search 扫描整个字符串并返回第一个成功的匹配。re.search(pattern, string, flags=0)
    # result = re.search(r'(.*)are(.*?)', a_string)
    # print(result)
    # print(result.group(0), 'group0')
    # print(result.group(1), 'group1')
    # print(result.group(2), 'group2')
    # Python 的re模块提供了re.sub用于替换字符串中的匹配项。

    # re.sub(pattern, repl, string, count=0, flags=0)
    result = re.match(r'', a_string)

    # compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
    #
    # 语法格式为：
    #
    # re.compile(pattern[, flags])
    # pattern = re.compile(r'(.*)are(.*?).*')
    # result = pattern.search(a_string)
    # print(result.group())
    # findall
    # 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果有多个匹配模式，则返回元组列表，如果没有找到匹配的，则返回空列表。
    #
    # 注意： match 和 search 是匹配一次 findall 匹配所有。
    #
    # 语法格式为：
    #
    # re.findall(pattern, string, flags=0)
    # 或
    # pattern.findall(string[, pos[, endpos]])
    # result1 = re.findall(r'\d+', 'runoob 123 google 456')
    #
    # pattern = re.compile(r'\d+')  # 查找数字
    # result2 = pattern.findall('runoob 123 google 456')
    # result3 = pattern.findall('run88oob123google456', 0, 10)
    #
    # print(result1)
    # print(result2)
    # print(result3)
    # !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
    # -*- coding: utf-8 -*-
    print("Content-type:text/html\n\n")
    print()
    print('<html>')
    print('<head>')
    print('<meta charset="utf-8">')
    print('<title>Hello Word！</title>')
    print('</head>')
    print('<body>')
    print('<h2>Hello Word!</h2>')
    print('</body>')
    print('</html>')


if __name__ == '__main__':
    main()
