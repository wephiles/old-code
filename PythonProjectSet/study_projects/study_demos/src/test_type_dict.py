#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime  :2024/09/03 22:40
# @Author      :wephiles@20866
# @IDE         :PyCharm
# @ProjectName :study_demos
# @FileName    :study_demos/test_type_dict.py
# @Description :This is description of this script.
# @Interpreter :Python 3.0+
# @Motto       :You must take your place in the circle of life!
# @AuthorSite  :https://github.com/wephiles or https://gitee.com/wephiles

"""
This file shows how to use "TypedDict".
"""

from typing import TypedDict, NotRequired, Required


class Coordinate(TypedDict):
    x: float
    y: float
    label: str
    category: NotRequired[str]


coordinate: Coordinate = {'x': 10, 'y': 10, 'label': 'l', 'category': 'c'}
# 如果不导入NotRequired的话，IDE会报错 -- 四个值必须全部写全
# 导入NotRequired后。这样写IDE就不会报错了
coordinate_1: Coordinate = {'x': 2, 'y': 5, 'label': 'r'}

Vote = TypedDict('Vote', {'for': int, 'against': int}, total=True)

Vote_1 = TypedDict('Vote_1', {'for': int, 'against': Required[int]},
                   total=True)

vote: Vote = {'for': 100, 'against': 250}
vote1: Vote_1 = {'for': 100}

# --END--
