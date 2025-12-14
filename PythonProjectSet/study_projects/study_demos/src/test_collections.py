#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime  :2024/09/03 19:12
# @Author      :wephiles@20866
# @IDE         :PyCharm
# @ProjectName :study_demos
# @FileName    :study_demos/test_collections.py
# @Description :This is description of this script.
# @Interpreter :Python 3.0+
# @Motto       :You must take your place in the circle of life!
# @AuthorSite  :https://github.com/wephiles or https://gitee.com/wephiles

import typing as t
import collections

from collections import namedtuple

CarMotto = namedtuple('Car', ['color', 'mileage', 'model'])
my_car = CarMotto(color='red', mileage='15', model='Corvette')
print(my_car.color)  # 输出: red

# --END--
