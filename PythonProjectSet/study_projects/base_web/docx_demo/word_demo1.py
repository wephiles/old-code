# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/16 016 16:51
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/word_demo1.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

import re
import docx
from docx.parts.image import ImagePart

# {rId5: "", rId6: "", ...}
doc_obj = docx.Document(r".\docx_files\demo.docx")

img_rel_dict = {}

# #################### 1. 获取ID和图片路径的对应关系 ####################

# 别问为什么 问就是看的老师写的 老师是看源码的 所以我也不知道为什么要这么写
for item in doc_obj.part.rels.values():
    # print(item)  # <docx.opc.rel._Relationship object at 0x000001A129101F90> --这样式的对象

    # print(item.target_part)  # 下面两行是这行打印语句的输出(截取了一部分)
    # # <docx.parts.image.ImagePart object at 0x000001CD50CB1FF0>
    # # <docx.parts.settings.SettingsPart object at 0x000001CD50CB2050>

    if type(item.target_part) == ImagePart:
        # print(item, item.rId, item.target_part.partname)
        img_rel_dict[item.rId] = item.target_part.partname

# #################### 2. 读取word文件 ####################
paragraphs = doc_obj.paragraphs
# 获取所有段落 p_obj对象 (读取xml文档并将文档格式处理)
for p_obj in paragraphs:
    # print(p.text, "\t", p.style.name)

    # 看看原始内容是什么
    # print(p_obj._p.xml)

    if "Graphic" in p_obj._p.xml:  # 代表这里面有图片
        # 是图片 获取图片id
        img_id = re.findall(r'<a:blip r:embed="(\w+)">', p_obj._p.xml)[0]

        # 找到图片的路径
        img_path = img_rel_dict[img_id]
        print(img_path)
    else:
        print(p_obj.text)

# --END--
