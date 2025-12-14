# -*- coding: utf-8 -*-
# @CreateTime : 2024/5/8 008 20:41
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/demo4.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# from xml.etree import ElementTree as ET
#
#
# # 打开文件
# tree = ET.parse(r"./files/xo.xml")
#
# # 获取根节点
# root = tree.getroot()
# print(root)  # <Element 'library' at 0x00000230F909D530>

# 通过网络获取的字符串 直接使用下面这种操作即可
# content = """
# <library>
#     <book id="1">
#         <title>XML Fundamentals</title>
#         <author>John Doe</author>
#         <year>2021</year>
#     </book>
#     <book id="2">
#         <title>Learning XML</title>
#         <author>Jane Smith</author>
#         <year>2022</year>
#     </book>
# </library>
# """
# root = ET.XML(content)
# print(root)

from xml.etree import ElementTree as ET

content = """
<library>
    <book id="1001">
        <title id="1">XML Fundamentals</title>
        <author>John Doe</author>
        <year>2021</year>
        <neighbor name="a"/>
    </book>
    <book id="1002">
        <title>Learning XML</title>
        <author>Jane Smith</author>
        <year>2022</year>
        <neighbor name="b"/>
    </book>
</library>
"""

# 获取根标签
root = ET.XML(content)
# print(root)
# print(root.tag)
#
# # 获取根标签的孩子标签
# for child in root:
#     # # 获取标签名
#     # child_tag = child.tag
#     # child_attrib = child.attrib
#     # print(child_tag, child_attrib)
#     for node in child:
#         print(node.tag, node.attrib, node.text)

# book_obj = root.find("book")
# print(book_obj.tag, book_obj.attrib)  # book {'id': '1'}
# title_obj = book_obj.find("title")
# print(title_obj.tag, title_obj.attrib, title_obj.text)


# for child in root.iter("year"):
#     print(child.tag, child.text)

year_obj = root.find("book").find("year")
year_obj.text = "2021-01-25"  # 修改
year_obj.set("update", '2024-02-06')  # 添加属性

# 删除节点
root.remove(root.find("book"))

# 写入文件保存
tree = ET.ElementTree(root)
tree.write("./files/new1.xml", encoding="utf-8")

# --END--
