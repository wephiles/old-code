# -*- coding: utf-8 -*-
# @CreateTime : 2024/5/26 026 13:12
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/demo5.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

from xml.etree import ElementTree as ET

# 创建根标签
root = ET.Element("family")

# # 创建节点大儿子
# son1 = ET.Element("son", attrib={"name": "son1"})
#
# # 创建小儿子
# son2 = ET.Element("son", attrib={"name": "son2"})
#
# # 大儿子中创建两个孙子
# grandson1 = ET.Element("grandson1", attrib={"name": "grandson1"})
# grandson2 = ET.Element("grandson2", attrib={"name": "grandson2"})
# son1.append(grandson1)
# son1.append(grandson2)
#
# # 把大小儿子添加到根节点中
# root.append(son1)
# root.append(son2)

# son1 = root.makeelement("son1", {"name": "son1"})
# son2 = root.makeelement("son2", {"name": "son2"})
#
# root.append(son1)
# root.append(son2)

son1 = ET.SubElement(root, "son1", {"name": "son1"})

grandson = ET.SubElement(son1, "grandson", {"name": "grandson"})

tree = ET.ElementTree(root)
tree.write("./files/son2.xml", encoding="utf-8", xml_declaration=True)

# --END--
