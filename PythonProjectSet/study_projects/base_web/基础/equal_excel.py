# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/15 015 21:33
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/equal_excel.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

from openpyxl.styles import Alignment, Border, Side, Font, PatternFill, Color
from openpyxl.workbook import Workbook

workbook_obj = Workbook()

sheet_0 = workbook_obj.worksheets[0]

# 数量
sheet_0["A1"] = 10
sheet_0["A2"] = 20
sheet_0["A3"] = 8

# 单价
sheet_0["B1"] = 3
sheet_0["B2"] = 8
sheet_0["B3"] = 9

# 写入公式
sheet_0["C1"] = "=A1*B1"
sheet_0["C2"] = "=A2*B2"
sheet_0["C3"] = "=A3*B3"

sheet_0["D1"] = "=sum(A1,B1)"
sheet_0["D2"] = "=sum(A2,B2)"
sheet_0["D3"] = "=sum(A3,B3)"

# sheet_0.delete_rows(idx=2, amount=1)  # 从第二行开始删除 删除的行数为1
# sheet_0.delete_columns(idx=3, amount=1)  # 从第三列开始删除 删除的列数为1

sheet_0.insert_rows(idx=1, amount=3)  # 从第二行开始删除 删除的行数为1
sheet_0.insert_cols(idx=1, amount=2)  # 从第三列开始删除 删除的列数为1

workbook_obj.save("./files/equal_excel.xlsx")

# --END--
