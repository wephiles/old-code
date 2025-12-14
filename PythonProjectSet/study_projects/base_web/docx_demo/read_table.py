# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/16 016 20:02
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/read_table.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

import docx

doc_obj = docx.Document("./docx_files/demo.docx")
table_obj = doc_obj.tables[0]


def get_table_list(table_obj):
    """
    获取表格数据
    Args:
        table_obj ():

    Returns:

    """
    table_list = []
    # 表格对象
    for row_obj in table_obj.rows:
        row_list = []
        for cell_obj in row_obj.cells:
            row_list.append(cell_obj.text)
        table_list.append(row_list)
    return table_list


print(get_table_list(table_obj))

# --END--
