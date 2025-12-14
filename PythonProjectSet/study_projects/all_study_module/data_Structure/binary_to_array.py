# -*- coding: utf-8 -*-
# @CreateTime : 2023/11/8 008 15:37
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/binary_to_array.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def level_order_traversal(root, tree: list, n: int):
        if not root:
            return 0
        queue = [root]
        array = []
        while queue:
            p = queue.pop(0)
            if p is not None:
                array.append(p.val)
                if p.left:
                    queue.append(p.left)
                else:
                    queue.append(None)
                if p.right:
                    queue.append(p.right)
                else:
                    queue.append(None)
            else:
                array.append(None)
        print(array)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    tree = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]
    n = 10
    # print(root.level_order_traversal(root, tree, 10))
    root.level_order_traversal(root, tree, 10)


main()

# from collections import deque
#
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# def tree2arr(root: TreeNode, arr: list, index: int):
#     if not root:
#         return index + 1
#     queue = deque([root])
#     while queue:
#         node = queue.popleft()
#         arr[index] = node.val
#         index += 1
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#     return index
#
#
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# # root.left.right = TreeNode(5)
# # root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
# array = []
# tree2arr(root, array, 1)

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# def level_order_traversal(root):
#     if not root:
#         return []
#
#     result = []
#     queue = [root]
#
#     while queue:
#         level = []
#         for i in range(len(queue)):
#             node = queue.pop(0)
#             if node:
#                 level.append(node.val)
#                 queue.append(node.left)
#                 queue.append(node.right)
#             else:
#                 level.append(None)
#
#         result.extend(level)
#
#     return result
#
#
# # 测试
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# # root.left.right = TreeNode(5)
# # root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
#
# print(level_order_traversal(root))

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 
# 
# def level_order_traversal(root):
#     if not root:
#         return []
#     queue = [root]
#     array = []
#     while queue:
#         p = queue.pop(0)
#         if p is None:
#             array.append(-1)
#         else:
#             array.append(p.val)
#             queue.append(p.left)
#             queue.append(p.right)
#     return array
# 
# 
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.right.right = TreeNode(5)
# 
# print(level_order_traversal(root))

# END
