# -*- coding: utf-8 -*-
# @CreateTime : 2024/2/22 022 10:57
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : testProject/demo1.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

# 假设我们有一个用户-物品交互的字典，键是用户ID，值是物品ID的集合
user_item_interactions = {
    'user1': {'item1', 'item2', 'item3'},
    'user2': {'item1', 'item2'},
    'user3': {'item2', 'item3', 'item4'},
}

# 创建一个空的倒排索引字典
item_user_index = {}

# 遍历用户-物品交互数据，填充倒排索引
for user, items in user_item_interactions.items():
    for item in items:
        if item not in item_user_index:
            item_user_index[item] = set()
        item_user_index[item].add(user)

# 现在item_user_index包含了用户-物品的倒排索引
print(item_user_index)

# END
