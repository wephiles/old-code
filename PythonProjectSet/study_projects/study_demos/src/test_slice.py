#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime  :2024/09/03 21:49
# @Author      :wephiles@20866
# @IDE         :PyCharm
# @ProjectName :study_demos
# @FileName    :study_demos/test_slice.py
# @Description :This is description of this script.
# @Interpreter :Python 3.0+
# @Motto       :You must take your place in the circle of life!
# @AuthorSite  :https://github.com/wephiles or https://gitee.com/wephiles

text: str = 'I am a robot!'
text_1: str = 'I am not a robot!'

my_slice = slice(None, 10)  # 相当于切片的[:10]

print(text[:10])
print(text[::10])  # Io
print(text[my_slice])
print(text_1[my_slice])

# 反转字符串
text_2: str = 'I am your father.'
my_slice_1 = slice(None, None, -1)  # 等同于切片的 [::-1] -- 也就是反转字符串
print(text_2[my_slice_1])  # 等同于切片的 [::-1] -- 也就是反转字符串
# --END--
