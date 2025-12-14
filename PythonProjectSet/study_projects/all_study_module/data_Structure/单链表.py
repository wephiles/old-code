# -*- coding: utf-8 -*-
# @CreateTime : 2023/8/27 027 22:09
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/单链表.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles


from typing import Optional


class Node(object):
    def __init__(self, val: int):
        self.val: int = val
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.next = None
        self.tail = self.head

    def init(self, data_list: list[int]):
        self.head = Node(data_list[0])
        self.head.next = None
        p = self.head
        for i in range(1, len(data_list)):
            p.next = Node(data_list[i])
            p = p.next

    def traverse(self):
        p = self.head
        while p.next is not None:
            p = p.next
            print(p.val, end='->')
        print()


"""
带头节点单链表：
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.dummy = ListNode()
        self.tail = self.dummy

    def traverse(self):
        cur = self.dummy.next
        while cur:
            print(cur.val, end=' -> ')
            cur = cur.next
        print('None')

    def delete_node(self, val):
        cur = self.dummy
        while cur.next and cur.next.val != val:
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next

    def insert_front(self, val):
        new_node = ListNode(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node
        self.tail = new_node

    def insert_tail(self, val):
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

# 测试代码
ll = LinkedList()
ll.insert_front(1)
ll.insert_front(2)
ll.insert_tail(3)
ll.insert_tail(4)
ll.traverse()  # 输出：2 -> 1 -> 3 -> 4 -> None
ll.delete_node(1)
ll.traverse()  # 输出：2 -> 3 -> 4 -> None
"""

# END
