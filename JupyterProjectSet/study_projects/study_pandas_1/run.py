# -*- coding: utf-8 -*-
# @CreateTime : 2024/7/4 004 21:55
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : study_pandas
# @FileName : study_pandas/run.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import pandas as pd


def main(num: int = 0) -> int:
    """
    main函数，整个项目的入口。
    Args:
        num (int): 参数

    Returns:
        int
    """
    print('start from', num)
    a_dict: dict = {
        'A': ['A1', 'A2', 'A3', 'A4'],
        'B': ['B1', 'B2', 'B3', 'B4'],
        'C': ['C1', 'C2', 'C3', 'C4'],
        'D': ['D1', 'D2', 'D3', 'D4'],
        'E': ['E1', 'E2', 'E3', 'E4'],
    }

    df = pd.DataFrame(a_dict)
    #
    # print(df)
    # #     A   B   C   D   E
    # # 0  A1  B1  C1  D1  E1
    # # 1  A2  B2  C2  D2  E2
    # # 2  A3  B3  C3  D3  E3
    # # 3  A4  B4  C4  D4  E4
    #
    # print(df['A'])
    # # 0    A1
    # # 1    A2
    # # 2    A3
    # # 3    A4
    # # Name: A, dtype: object
    #
    # print(df[['A', 'B']])
    # # A   B
    # # 0  A1  B1
    # # 1  A2  B2
    # # 2  A3  B3
    # # 3  A4  B4
    #
    # print(df.loc[0:3, 'A':'C'])
    # #     A   B   C
    # # 0  A1  B1  C1
    # # 1  A2  B2  C2
    # # 2  A3  B3  C3
    # # 3  A4  B4  C4
    print(df.iloc[0:3])
    #     A   B   C   D   E
    # 0  A1  B1  C1  D1  E1
    # 1  A2  B2  C2  D2  E2
    # 2  A3  B3  C3  D3  E3

    print(df.loc[0:3])
    #     A   B   C   D   E
    # 0  A1  B1  C1  D1  E1
    # 1  A2  B2  C2  D2  E2
    # 2  A3  B3  C3  D3  E3
    # 3  A4  B4  C4  D4  E4

    print(df.iloc[0:3, 1:2])
    #     B
    # 0  B1
    # 1  B2
    # 2  B3

    # print(df.loc[0:3, 1:2])  # 报错

    # df_1 = pd.Series([1, 2, 3, 4, 5], index=['A', 'B', 'C', 'D', 'E'], name='num')

    # # print(df_1)
    # # A    1
    # # B    2
    # # C    3
    # # D    4
    # # E    5
    # # dtype: int64

    # print(df_1['A'])  # 1

    # print(df_1[['A', 'B']])
    # # A    1
    # # B    2
    return 0


if __name__ == '__main__':
    main(10)

# --END--
