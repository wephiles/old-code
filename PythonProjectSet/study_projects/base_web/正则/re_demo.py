# -*- coding: utf-8 -*-
# @CreateTime : 2024/3/30 030 21:24
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/re_demo.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

# import re
#
# # re_str = "1[3|5|8|9]\d{9}"  # 手机号
# re_str = "\w+@\w+.\w+"  # 邮箱
#
#
# text = """正则表达式，又称规则表达式，（Regular Expression，在代码中常简写为regex、regexp或RE），是一种文本模式，
# 包括普通字符（例如，a到z之间的字母）和特殊字符（称为“元字符”），是计算机科学的一个概念。正则表达式是对字符串（包括普
# 通字符和特殊字符）操作的一种逻辑公式，就是用事先定义好的一些特定字符以及这些特定字符的组合，组成一个“规则字符串”，这
# 个“规则字符串”用来表达对字符串的一种过滤逻辑。正则表达式用来检索、替换那些符合某个模式（规则）的文本，通常被用来检索、
# 替换那些符合某个模式（规则）的文本。正则表达式可以从一个基础字符串中根据一定的匹配模式替换文本中的字符串、验证表单、提
# 取字符串等等，许多程序设计语言都支持利用正则表达式进行字符串操作。楼主:瑾瑜，电话 18866666666，邮箱: 12345679@163.com。
# 求点赞求转发，求一键三连！！！"""
#
# phone_number = re.findall(re_str, text)
#
# print(phone_number)

# import re
#
# text = """root-ad13main-c4ompu423416ter science-aad234main"""
#
# data_list = re.findall(r"\d", text)  # 找 ha hb hc 从前向后找
# print(data_list)

# import re
# 
# text = """你好巴拉巴拉 biubiubiu computer science good morning longArc架构 计算机科学与技术 华为牛逼 
# 打倒美帝国主义纸老虎 日本鬼子不得好死 祝没有真心反对日本核污水排海的日本人全都收到核辐射而死 hahaha 耶 2024年3月10日"""
# 
# data_list = re.findall("计算机\w+技术", text)
# print(data_list)

# import re
#
# text = """正则表达式，又称规则表达式，（Regular Expression，在代码中常简写为regex、regexp或RE），是一种文本模式，
# 包括普通字符（例如，a到z之间的字母）和特殊字符（称为“元字符”），是计算机科学的一个概念。18866root太牛逼了。正则表达式是对字符串（包括普
# 通字符和特殊字符）操作的一种逻辑公式，就是用事先定义好的一些特定字符以及这些特定字符的组合，组成一个“规则字符串”，这
# 个“规则字符串”用来表达对字符串的一种过滤逻辑。正则表达式用来检索、替换那些符合某个模式（规则）的文本，通常被用来检索、
# 替换那些符合某个模式（规则）的文本。正则表达式可以从一个基础字符串中根据一定的匹配模式替换文本中的字符串、验证表单、提
# 取字符串等等，许多程序设计语言都支持利用正则表达式进行字符串操作。楼主:瑾瑜，电话 18866666666，邮箱: 123456789@163.com。
# 求点赞求转发，求一键三连！！！18866668888"""
#
# data_list = re.findall(r"18866(6\d{5}|r\w+太)", text)
# print(data_list)

# import re
#
# text = "大小逗2B最逗3B欢乐"
#
# regular = r"逗\dB"
# data_list = re.findall(regular, text)
# print(data_list)
#
# data_list = re.match(regular, text)
# print(data_list)

# import re
#
# regular = r"大小逗\dB"
# text = "大小逗2B最逗3B欢乐"
# data_list = re.match(regular, text)
# print(data_list)  # None

# import re
#
# regular = r"大小逗\dB"
# text = "大小逗2B最逗3B欢乐"
# data_obj = re.match(regular, text)
# data = data_obj.group()
# print(data)

# import re
#
# regular = r"逗\dB"
# text = "大小逗2B最逗3B欢乐"
# data_list = re.search(regular, text)
# print(data_list)  #

# import re
# import sys
#
# print("请输入手机号：")
# mobile_number = input(">>> ")
# mobile_number = mobile_number.strip()
# # 验证手机号码是否合法
# regular = r"^1[3|5|8|9]\d{9}$"
# if re.match(regular, mobile_number):
#     print("手机号码合法, ", mobile_number)
# else:
#     print("手机号码非法", mobile_number, file=sys.stderr)

# import re
#
# text = "1+8-7+18-20"
# data_list = re.split("[+-]", text)
# print(data_list)  # ['大小逗', '最逗', '欢乐']

# import requests
#
# url = r"https://search.douban.com/movie/subject_search?search_text=%E7%83%AD%E9%97%A8&cat=1002"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/122.0.0.0 Safari/537.36",
# }
#
# # 返回的所有response数据都拿到
# res = requests.get(url=url, headers=headers)
#
# # 原始的响应体
# text = res.content.decode("utf-8")
# print(text)

import requests

url = r"https://search.douban.com/movie/subject_search?search_text=%E7%83%AD%E9%97%A8&cat=1002"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.0.0 Safari/537.36",
}

# 返回的所有response数据都拿到
res = requests.get(url=url, headers=headers)

print(res.text)

# --END--
