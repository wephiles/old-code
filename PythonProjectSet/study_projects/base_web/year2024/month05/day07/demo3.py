# -*- coding: utf-8 -*-
# @CreateTime : 2024/5/8 008 20:06
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/demo3.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

import configparser

config = configparser.ConfigParser()
config.read(r'./files/config.ini', encoding='utf-8')

# # 获取所有的节点section
# config_sections = config.sections()
# print(config_sections)

# # 获取节点下面的键值对
# config_keys_values = config.items("database")
# print(config_keys_values)
#
# for key, value in config_keys_values:
#     print(key, value)

# # 获取某个节点下面的键对应的值
# value = config.get("database", "DatabaseUser")
# print(value)

# 其他功能

# # 判断一个节点是否存在
# res = config.has_section("port")
# print(res)

# # 添加一个节点
# config.add_section("group")

# # 添加节点的键值
# config.set("group", "groupName", "group1")
# config.set("email", "groupName", "group1")
#
# # 将修改写入外存文件保存
# config.write(open(r"./files/config.ini", "w", encoding="utf-8"))

# 删除
config.remove_section("group")
config.remove_option("email", "groupname")
config.write(open(r"./files/config.ini", "w", encoding="utf-8"))

# --END--
