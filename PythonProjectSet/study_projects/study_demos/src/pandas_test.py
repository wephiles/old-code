# -*- coding: utf-8 -*-
# @CreateTime : 2024/08/17 14:40
# @Author: wephiles@20866
# @IDE: PyCharm
# @ProjectName: study_demos
# @FileName: study_demos/pandas_test.py
# @Description: This is description of this script.
# @Interpreter: python 3
# @Motto: You must take your place in the circle of life!
# @AuthorSite: https://github.com/wephiles or https://gitee.com/wephiles

import pandas as pd

a_dict: dict = {
    'A': [1, 2, 3, 4, 5, 6],
    'B': [11, 12, 13, 14, 15, 16],
    'C': [111, 112, 113, 114, 115, 116]
}

df = pd.DataFrame(a_dict)

df.to_excel('./test.xlsx', index=False)

# --END--
