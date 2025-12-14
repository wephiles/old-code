# -*- coding: utf-8 -*-
# @CreateTime : 2021/11/26 16:54
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : LL.py
# @Software : PyCharm
# 下面是学习面向对象以及单链表


class LinkNode(object):  # 结点类
    def __init__(self):  # 默认构造函数
        self.Data = 0
        self.next = None


class SingleLinkList(object):  # 单链表类
    def __init__(self):  # 默认构造函数
        self.Header = LinkNode()  # 首结点
        self.Tail = None   # 尾结点
        self.len = 0
        self.Header.Data = self.len  # 利用空的header.data域存放链表长度

    def __del__(self):  # 析构函数
        print('Destructor call !!!')

    def init_single_linklist(self):  # 初始化单链表
        self.Header.next = None
        self.Tail = None
        self.Header.Data = 0
        self.len = 0

    def is_empty(self):  # 判断单链表是不是非空
        if self.len <= 0:
            return True
        else:
            return False

    def length_single_linklist(self):  # 返回链表的长度
        return self.len

    def add_list(self, li):   # 在链表的后面添加一个列表，成为单链表
        for i in li:
            self.add_element_end(i)
        return True

    def clear_single_linklist(self):  # 清除链表的所有元素
        if self.is_empty():
            print('链表是空的，无法删除！！！')
            return False
        pointer = self.Header
        while pointer.next is not None:
            pointer = pointer.next
            del pointer.Data
        self.Header.next = None
        self.len = 0
        return True

    def destroy_single_linklist(self):  # 销毁单链表
        self.clear_single_linklist()
        del self.Header
        print('销毁单链表成功！！！')

    def add_element_head(self, a):  # 在链表的头部插入一个元素
        a_node = LinkNode()  # 新建一个结点
        a_node.Data = a  # 将这个结点的值赋值为用户传入的值
        pointer = self.Header
        if self.len == 0:
            a_node.next = None
            pointer.next = a_node
        else:
            a_node.next = pointer.next
            pointer.next = a_node
        self.len += 1
        return a

    def add_element_middle(self, pos, b):
        # 在链表的中间(第pos个位置后面，
        # pos不是偏移，而是从1开始的绝对位置)插入一个元素
        # 1 <= pos <= len
        if self.len in [0, 1]:
            print('这个链表的长度不足2，所以在链表进行尾部加入元素')
            self.add_element_end(b)
            return b
        if pos < 1 or pos >= self.len:
            print('您输入的位置超过了范围！')
            return False
        b_node = LinkNode()
        b_node.Data = b
        pointer = self.Header
        for i in range(0, pos):
            pointer = pointer.next
        b_node.next = pointer.next
        pointer.next = b_node
        self.len += 1
        return b

    def add_element_end(self, c):  # 在链表的尾部插入一个元素
        pointer = self.Header
        while pointer.next is not None:
            pointer = pointer.next
        c_node = LinkNode()
        c_node.Data = c
        c_node.next = None
        pointer.next = c_node
        self.len += 1
        return c

    def get_offset(self, e):  # 找某个元素的偏移量
        if self.is_empty():
            print('单链表是空的，没有元素')
        pointer = self.Header
        if pointer.next.Data == e:
            return 0
        i = 0
        while pointer.next is not None:
            pointer = pointer.next
            i += 1
            if pointer.Data == e:
                return i - 1
            if i > self.len:
                break
        return False

    def get_element(self, pos):  # 查找链表中第pos个位置的元素(pos为绝对位置，从1开始计数)
        if self.is_empty() or pos < 1 or pos > self.len:
            print('单链表为空或者您输入的数据超出范围！！！')
            return False
        pointer = self.Header
        for i in range(0, pos):
            pointer = pointer.next
        return pointer.Data

    def precursor_element(self, e):  # 寻找e的前驱元素
        if self.is_empty():
            print('单链表是空的，没有元素')
            return False
        pointer1 = self.Header.next
        pointer2 = self.Header
        if self.len == 1:
            print('您的单链表只有一个元素，不能找到前驱元素！！！')
        if pointer1.Data == e:
            print('您所要找的元素在单链表中是第一个元素，没有前驱元素！！！')
            return False
        i = 0
        while pointer1.next is not None:
            pointer2 = pointer2.next
            pointer1 = pointer1.next
            if pointer1.Data == e:
                i = 1
                return pointer2.Data
        if i == 0:
            print('找不到您要查找的元素！！！')
            return False

    def successor_element(self, e):  # 寻找e的后继元素
        if self.is_empty():
            print('单链表是空的，没有元素')
            return False
        pointer3 = self.Header.next
        pointer4 = self.Header
        if pointer3.Data == e:
            if pointer3.next is not None:
                return pointer3.next.Data
            else:
                print('您的单链表只有一个元素，不能找到后继元素！！！')
                return False
        i = 0
        while pointer3.next is not None:
            pointer4 = pointer4.next
            pointer3 = pointer3.next
            if pointer4.Data == e:
                i = 1
                return pointer3.Data
        if pointer3.next is None and pointer3.Data == e:
            print('您要找的元素的前驱元素是最后一个元素，没有后继元素！！！')
        if i == 0:
            print('不存在你要找的元素！！！')
            return False

    # 这个函数有问题，需要再改进
    # def delete_element(self, e):  # 删除一个元素
    #     if self.is_empty():
    #         print('单链表是空的！！！')
    #         return False
    #     pointer = self.Header
    #     pointer_temp = self.Header.next
    #     i = 0
    #     while pointer_temp.next is not None:
    #         pointer_temp = pointer_temp.next
    #         pointer = pointer.next
    #         if pointer_temp.Data == e:
    #             q = pointer.next
    #             pointer.next = q.next
    #             q.next = None
    #             del q.Data
    #             i = 1
    #             self.len -= 1
    #             break
    #     if i == 0:
    #         print('没有你所要找的数据！！！')
    #         return False
    #     return e

    def delete_element_offset(self, pos):  # 删除一个位置的元素
        if self.is_empty():
            print('单链表是空的！！！')
            return False
        if pos < 1 or pos > self.len:
            print('超过了范围！！！')
            return False
        pointer = self.Header
        for i in range(0, pos):
            pointer = pointer.next
        q = pointer.next
        pointer.next = q.next
        q.next = None
        del q.Data
        self.len -= 1

    def traverse_single_linklist(self):  # 遍历单链表
        if self.is_empty():
            print('链表是空的！！！')
            return False
        pointer = self.Header
        print('Header ->', end=' ')
        while pointer.next is not None:
            pointer = pointer.next
            print(pointer.Data, end=' -> ')
        print('None')
        return True


# 测试单链表
def main():
    x = SingleLinkList()
    # x.init_single_linklist()
    # print('现在链表的长度是：{}'.format(x.length_single_linklist()))
    # print('链表是空的：{}'.format(x.is_empty()))
    # print('下面进行添加链表元素:')
    x.add_list([2, 5, 6, 0, 8, 9, 10, 15])
    # x.add_element_end(2)
    # x.add_element_head(5)
    # x.add_element_head(4)
    # x.add_element_end(3)
    # x.add_element_middle(5, 20)
    # print('现在链表的长度是：{}'.format(x.length_single_linklist()))
    # print('下面遍历链表:')
    # x.traverse_single_linklist()
    # x.clear_single_linklist()
    # x.traverse_single_linklist()
    # print('现在链表的长度是：{}'.format(x.length_single_linklist()))
    # print('链表是空的：{}'.format(x.is_empty()))
    # x.traverse_single_linklist()
    # x.destroy_single_linklist()
    x.traverse_single_linklist()
    # print(x.get_offset(15))
    # print(x.get_element(7))
    # print(x.precursor_element(17))
    # print(x.successor_element(151))
    # x.delete_element_offset(3)
    # x.delete_element(2)
    x.delete_element_offset(5)
    x.traverse_single_linklist()


if __name__ == '__main__':
    main()












