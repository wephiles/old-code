# -*- coding: utf-8 -*-
# @CreateTime : 2022/1/10 17:27
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : a_class.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe


class People:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

    def sum_a_b(self):
        return self.a + self.b

    def sum_a_b_c(self):
        return self.a + self.b + self.c

    def run_run(self):
        print(self.a, self.b, self.c)


if __name__ == '__main__':
    x = People()
    x.a = 10
    x.b = 15
    x.c = 20
    print(x.sum_a_b_c())
    pass
