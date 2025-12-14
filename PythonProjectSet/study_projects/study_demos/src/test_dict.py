#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime  :2024/09/03 22:37
# @Author      :wephiles@20866
# @IDE         :PyCharm
# @ProjectName :study_demos
# @FileName    :study_demos/test_dict.py
# @Description :This is description of this script.
# @Interpreter :Python 3.0+
# @Motto       :You must take your place in the circle of life!
# @AuthorSite  :https://github.com/wephiles or https://gitee.com/wephiles

"""
This file show interesting dict.
"""

values = ('a1', 'b2', 'c3')  # print(dict(values))
print(dict(values))

values = ('a1', 'b2', 'c')
# ValueError: dictionary update sequence element #2 has length 1; 2 is required
print(dict(values))

# --END--
