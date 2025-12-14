# -*- coding: utf-8 -*-
# @CreateTime : 2024/08/17 21:54
# @Author: wephiles@20866
# @IDE: PyCharm
# @ProjectName: study_demos
# @FileName: study_demos/quick_start.py
# @Description: This is description of this script.
# @Interpreter: python 3
# @Motto: You must take your place in the circle of life!
# @AuthorSite: https://github.com/wephiles or https://gitee.com/wephiles

# import streamlit as st
# import pandas as pd
#
# upload_file = st.file_uploader('支持的文件：excel文件', type=['xlsx'])
# if upload_file is None:
#     st.stop()
#
#
# # 使文件只在我们选择新文件的时候执行 -- 使用装饰器，表明这是个缓存函数
# @st.cache_data
# def load_data(file):
#     print('加载数据')
#     return pd.read_excel(upload_file)
#
#
# df = load_data(upload_file)
#
# # # 直接显示数据
# # st.dataframe(df)
#
# names = list(df.keys())
# # 下拉列表
# sheet_SELECTS = st.multiselect('工作表', names, [])
#
# if len(sheet_SELECTS) == 0:
#     st.stop()
#
# # 多选下拉框
# tabs = st.tabs(sheet_SELECTS)
# for tab, name in zip(tabs, sheet_SELECTS):
#     with tab:
#         new_df = df[name]
#         st.dataframe(new_df)


# --END--
