# -*- coding: utf-8 -*-
# @CreateTime : 2023/11/15 015 16:40
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/根到叶子结点最长路径.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longest_path(self, root: TreeNode) -> int:
        self.res = 0
        self.path= []
        self.dfs(root)
        return self.res

    def dfs(self, node: TreeNode) -> int:
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        max_len = max(left, right) + 1
        if max_len > self.res:
            self.res = max_len
            if left > right:
                self.path = [node.val] + self.path
            else:
                self.path = [node.val] + self.path[::-1]
        return max_len

    def print_longest_path(self, root: TreeNode):
        self.longest_path(root)
        print("最长路径为：", end="")
        for i in range(len(self.path)):
            print(self.path[i], end="")
            if i != len(self.path) - 1:
                print("->", end="")
        print()


# 测试
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    # root.left.right.right = TreeNode(11)
    # root.right.left.left = TreeNode(12)
    # root.right.left.right = TreeNode(13)
    # root.right.right.left = TreeNode(14)
    # root.right.right.right = TreeNode(15)
    #            1
    #     2             3
    #  4    5       6       7
    # 8 9  10 11  12 13  14   15

    s = Solution()
    s.print_longest_path(root)

# END
