# -*- coding: utf-8 -*-
# @CreateTime : 2024/3/23 023 21:51
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/os_demo.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

# import os
#
# path = os.path.join("x1", "x2", "x3", "db.txt")
# print(path)  # 会根据自己的操作系统生成路径

# import os
# 
# file_path = r"x1\x2\x3\db.txt"
# v1 = os.path.dirname(file_path)
# print(v1)

# import os
# res = os.path.abspath("xx")
# print(res)

# import os
#
# path = os.path.join("db", "2021", "11月份")
# os.makedirs(path)

# import os
#
#
# path = os.path.join("log.txt")
# os.remove(path)


# import os
# # import shutil
#
# if os.path.isdir("commons"):
#     print("yes")
# else:
#     print("no")
#
# if os.path.isdir("commons/xx"):
#     print("yes")
# else:
#     print("no")

# import os
#
# db_path = os.path.join("db", "users", "account.txt")
# # 确保文件目录已存在，如果不存在需要创建。
# folder_path = os.path.join("db", "users")
# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)
# while True:
#     user = input("用户名>>> ")
#     if user.upper() == "Q":
#         break
#     line = "{}\n".format(user)
#     with open(db_path, "a", encoding="utf-8") as fp:
#         fp.write(line)

# import os
# from pprint import pprint
# 
# target_folder_path = r"D:\备份-桌面\2024.03.23调剂"
# key = "自我介绍"
# 
# data_list = os.walk(target_folder_path)
# # pprint(data_list)
# for this_folder, folder_list, file_list in data_list:
#     for name in file_list:
#         if key in name:
#             print(os.path.join(this_folder, name))
import numpy as np

# 创建一个用户-物品矩阵，表示用户对物品的评分
user_item_matrix = np.array([
    [3, 1, 2, 3, 0],
    [4, 0, 0, 1, 1],
    [0, 2, 3, 0, 4],
    [1, 0, 0, 2, 3]
])

# 计算物品之间的相似度矩阵
def item_similarity_matrix(user_item_matrix):
    num_items = user_item_matrix.shape[1]
    item_sim_matrix = np.zeros((num_items, num_items))

    for i in range(num_items):
        for j in range(num_items):
            if i == j:
                continue
            common_users = np.logical_and(user_item_matrix[:, i] != 0, user_item_matrix[:, j] != 0)
            if np.sum(common_users) == 0:
                item_sim_matrix[i, j] = 0
            else:
                item_sim_matrix[i, j] = np.dot(user_item_matrix[:, i], user_item_matrix[:, j]) / (np.linalg.norm(user_item_matrix[:, i]) * np.linalg.norm(user_item_matrix[:, j]))

    return item_sim_matrix

# 预测用户对物品的评分
def predict(user_item_matrix, item_sim_matrix):
    num_users = user_item_matrix.shape[0]
    num_items = user_item_matrix.shape[1]
    pred_matrix = np.zeros((num_users, num_items))

    for i in range(num_users):
        for j in range(num_items):
            if user_item_matrix[i, j] != 0:
                continue
            pred_scores = np.dot(user_item_matrix[i], item_sim_matrix[:, j]) / np.sum(np.abs(item_sim_matrix[:, j]))
            pred_matrix[i, j] = pred_scores

    return pred_matrix

# 计算物品相似度矩阵
item_sim_matrix = item_similarity_matrix(user_item_matrix)
print("Item Similarity Matrix:")
print(item_sim_matrix)

# 预测用户对物品的评分
pred_matrix = predict(user_item_matrix, item_sim_matrix)
print("Predicted User-Item Matrix:")
print(pred_matrix)

# --END--
