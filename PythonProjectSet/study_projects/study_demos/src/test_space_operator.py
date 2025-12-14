#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime  :2024/09/04 19:07
# @Author      :wephiles@20866
# @IDE         :PyCharm
# @ProjectName :study_demos
# @FileName    :study_demos/test_space_operator.py
# @Description :This is description of this script.
# @Interpreter :Python 3.0+
# @Motto       :You must take your place in the circle of life!
# @AuthorSite  :https://github.com/wephiles or https://gitee.com/wephiles

x: int = 2
y: int = 3

result: int = (x > y) - (x < y)
print(result)
print(int(True - False))
print(int(False - False))

# --END--
