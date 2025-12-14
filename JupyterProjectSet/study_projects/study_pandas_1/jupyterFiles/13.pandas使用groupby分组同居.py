# -*- coding: utf-8 -*-
# @CreateTime : 2024/7/5 005 20:26
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : study_pandas
# @FileName : study_pandas/13.pandas使用groupby分组同居.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

"""
pandas怎样实现 groupby 分组统计
类似SQL
select city, max(temperature) from city_weather groupby city;

groupby:先对数据分组，然后在每个分组上应用聚合函数、转换函数。

本例演示：
1. 分组使用聚合函数作数据统计
2. 遍历groupby的结果理解执行流程
3. 实例分组探测天气数据
"""

import pandas as pd
import numpy as np

# # 加上下面这一句，能在jupyter notebook展示matplot图表
# %matplotlib inline

df = pd.DataFrame(
    {
        'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar'],
        'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
        'C': np.random.randn(8),
        'D': np.random.randn(8),
    }
)
# print(df)
# #      A      B         C         D
# # 0  foo    one  1.259443  0.732798
# # 1  bar    one -0.721566 -1.250820
# # 2  foo    two -0.350285 -0.770548
# # 3  bar  three  0.650063  0.976396
# # 4  foo    two  0.747344 -0.085171
# # 5  bar    two  1.763211 -0.433900
# # 6  foo    one -1.195779  0.931139
# # 7  bar  three  0.151585  1.142441

# 1. 分组使用聚合函数作数据统计
# 1.1 单个列groupby，查询所有数据列的统计
# 我们可以看到，groupby的‘A’变成了数据的索引列
res = df.groupby('A').sum()
print(res)

# # 1.2 多个列groupby 查询所有数据列的统计
# res = df.groupby(['A', 'B'], as_index=False).mean()
# print(res)

# 2.


# --END--
