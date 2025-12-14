# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/21 021 13:41
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/practice1.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

# class Account:
#
#     def __init__(self):
#         self.name = None
#
#     def info(self):
#         """
#         打印用户信息
#         Returns:
#
#         """
#         print("用户名：", self.name)
#
#     def account(self):
#         """
#         打印用户账单
#         Returns:
#
#         """
#         pass
#
#     def buy_pillow(self):
#         """
#         购买抱枕
#         Returns:
#
#         """
#         pass
#
#     def login(self):
#         user = input("请输入用户名：")
#         password = input("请输入密码：")
#         if password == "123456":
#             self.name = user
#             while True:
#                 print("1 查看用户信息 2 查看用户啊账单 3 购买抱枕")
#                 num_choose = int(input("""请输入选项："""))
#                 if num_choose == 1:
#                     self.info()
#                 elif num_choose == 2:
#                     self.account()
#                 elif num_choose == 3:
#                     self.buy_pillow()
#                 else:
#                     print("输入错误，请重新输入！")
#                 break
#             print("登录成功！")
#         else:
#             print("登录失败！")
#
#
# obj = Account()
# obj.login()

# import demo1
#
# x = demo1.Foo("computer")
#
# x.display()

# data_list = []
#
# for i in range(1, 301):
#     data_list.append("alex-%s" % i)
#
# page_size = 10
#
# print("请输入要查看的页码，输入q/Q退出。")
# while True:
#
#     page_num_str = input(">>> ")
#     if page_num_str.upper() == "Q":
#         break
#     page_num = int(page_num_str)
#     page_start_index = (page_num - 1) * page_size + 1
#     page_end_index = page_num * page_size
#     for item in range(page_start_index - 1, page_end_index):
#         print(data_list[item], end=" ")
#     print()


# class Pagination(object):
#     """
#     处理分页类
#     """
#
#     def __init__(self, total_page_num):
#         """
#         初始化分页类
#         Args:
#             total_page_num (): 总页数
#         """
#         self.total_page_num = total_page_num
#         self.page_size = 2
#
#     def get_start_index(self):
#         """
#         获取开始索引
#         Returns:
#
#         """
#         page_start_index = (self.total_page_num - 1) * self.page_size + 1
#         return page_start_index
#
#     def get_end_index(self):
#         """
#         获取结束索引
#         Returns:
#
#         """
#         page_end_index = self.total_page_num * self.page_size
#         return page_end_index

class Pagination(object):
    """
    处理分页类
    """

    def __init__(self, current_page_num, page_size=10, ):
        """
        初始化分页类
        Args:
            current_page_num (int): 当前页数
            page_size (int): 一页有多少条数据
        """
        self.current_page_num = current_page_num
        self.page_size = page_size

    @property
    def start(self):
        """
        获取开始索引
        Returns:

        """
        return (self.current_page_num - 1) * self.page_size

    @property
    def end(self):
        """
        获取结束索引
        Returns:

        """
        return self.current_page_num * self.page_size

    def show(self, data_list):
        """
        打印分页的那一页的数据
        Returns:

        """
        page_start_index = self.start
        page_end_index = self.end
        print(data_list[page_start_index:page_end_index])


def main() -> int:
    data_list = []

    for i in range(1, 301):
        data_list.append("alex-%s" % i)

    print("请输入要查看的页码，输入q/Q退出。")
    while True:
        page_num_str = input(">>> ")
        if page_num_str.upper() == "Q":
            break
        page_num = int(page_num_str)

        pagination_obj = Pagination(page_num, page_size=10)
        pagination_obj.show(data_list)

    return 0


if __name__ == '__main__':
    main()

# --END--
