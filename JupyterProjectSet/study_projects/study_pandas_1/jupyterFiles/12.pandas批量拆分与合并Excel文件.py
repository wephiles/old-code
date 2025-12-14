# -*- coding: utf-8 -*-
# @CreateTime : 2024/7/4 004 21:08
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : study_pandas
# @FileName : study_pandas/12.pandas批量拆分与合并Excel文件.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

"""
pandas批量拆分Excel与合并Excel

实例演示：
1. 将一个大的excel等分拆分成多个excel
2. 将多个小Excel合并成一个大的Excel并标记来源
"""

from pprint import pprint
import pandas as pd
import os

work_dir = '../data/course_datas/c15_excel_split_merge'
splits_dir = f'{work_dir}/splits'
# **************************************************************************
# if not os.path.exists(splits_dir):
#     os.mkdir(splits_dir)
#
# df_source = pd.read_excel(f'{work_dir}/crazyant_blog_articles_source.xlsx')
# # print(df_source.head(5))
# # print(df_source.index)  # RangeIndex(start=0, stop=258, step=1)
# # print(df_source.shape)  # (258, 3)
#
# # 计算总行数
# total_row_num = df_source.shape[0]
#
# # 将一个大excel等分拆成多个excel
# # 使用df.iloc方法，将一个大的DataFrame拆分成多个小的DataFrame
#
# # 计算拆封后的每个excel的行数
#
# # 这个大excel会拆分给这几个人
# user_name = ['xiao_deng', 'xiao_mei', 'xiao_huang', 'xiao_liang', 'xiao_bu', 'xiao_fu']
# # 每个人的任务数
# split_size = total_row_num // len(user_name)
# if total_row_num % split_size != 0:
#     split_size += 1
#
# df_subs: list = []
# for index, user_name in enumerate(user_name):
#     # iloc的开始索引
#     begin = index * split_size
#     end = begin + split_size
#     # df按照 iloc 拆分
#     df_sub = df_source.iloc[begin:end]
#     # 将每个子df存入列表
#     df_subs.append((index, user_name, df_sub))
# # 将每个df存入到exce
# for index, user_name, df_sub in df_subs:
#     file_name = f'{splits_dir}/crazyant_blog_articles_{index}_{user_name}.xlsx'
#     df_sub.to_excel(file_name, index=False)
# **************************************************************************

# 合并多个Excel表格为一个excel表格
# 1. 遍历文件夹，找到要合并的所有Excel文件列表
# 2. 分别读取到df，给每一个df添加一列用来标记来源
# 3. 使用pd。concat来批量合并
# 4. 将合并后的excel输出到excel


# 遍历文件夹，得到要合并的Excel名称列表
excel_names: list = []
for excel in os.listdir(splits_dir):
    excel_names.append(excel)

# 分别读取到df中
df_list = []
for excel in excel_names:
    excel_path = f'{splits_dir}/{excel}'
    df_split = pd.read_excel(excel_path)
    user_name = excel.replace("crazyant_blog_articles", "").replace(".xlsx", "")[3:]
    # print(excel, user_name)  # crazyant_blog_articles_0_xiao_deng.xlsx xiao_deng
    df_split['user_name'] = user_name
    df_list.append(df_split)

# 使用pd。concat进行合并
df_merged = pd.concat(df_list)
# print(df_merged.shape)
# print(df_merged.head(6))
# print(df_merged.value_counts())
# print(df_merged.value_counts().head())

# 将合并的输出到Excel
df_merged.to_excel(f'{work_dir}/crazyant_blog_articles_merged_1.xlsx', index=False)

# --END--
