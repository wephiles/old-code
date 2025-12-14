# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/17 017 12:01
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/docx_modify.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles


import docx
from docx.parts.image import ImagePart

doc_obj = docx.Document(r".\docx_files\demo.docx")
tb_obj = doc_obj.tables[0]

col_obj = tb_obj.columns[1]
for cell in col_obj.cells:
    cell._element.getparent().remove(cell._element)

doc_obj.save(r".\docx_files\demo_modified_7.docx")

# --END--
