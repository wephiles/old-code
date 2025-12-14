# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/22 13:10:10
# @Project: Pycharm_Project_Set
# @File : class_.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun


# class People:
#     name = ' '
#
#
# class Person(object):
#     name = ' '
#
#
# if __name__ == '__main__':
#     print(People)  # <class '__main__.People'>
#     print(Person)  # <class '__main__.Person'>
#
#     x = People()
#     print('People', dir(x))
#
#     y = Person()
#     print('Person', dir(y))
#
#     # 我们发现两者一样！！！
#     pass


# 类方法 ： 在方法上一行加一个 @classmethod 装饰器 cls参数就类似于self传入，
# 于是 cls()就相当于是这个类 详情见 https://www.cnblogs.com/king-lps/p/12597680.html
# 实例方法和类方法具体调用看：text.txt


# class People(object):
#     # 如果同样的属性名称同时出现在实例和类中，则属性查找会优先选择实例
#     name = 'Jerry'
#     # 所有实例都可以对其进行操作，共享
#     # 静态变量 可以被静态方法和类方法调用 所有实例共享的类变量
#
#     def __init__(self, b, c):
#         # 实例变量 静态方法和类方法不能调用
#         # 每个实例唯一的实例变量 每个实例有每个实例的对实例变量的操作
#         self.b = b
#         self.__weight = 200
#         self.c = c
#         print(People.name)
#         print()
#
#     def write(self):  # 不能调用
#         print('Write something!', end=' ')
#         print(self.b, self.c)
#         print(People.name)
#         print()
#
#     @staticmethod
#     def eat(g):  # 不能调用实例变量，但是可以调用静态变量
#         print('eat ', g)
#         print(People.name)
#         print()
#
#     @classmethod
#     def speak(cls, e, f):
#         print('hello')
#         print(e, f)
#         print(cls(1, 3).b, cls(1, 3).c)
#         print(cls(1, 3).name)
#         print(People.name)
#         print()
#
#
# class Person(People):
#     pass


class Reverse(object):
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

    pass


def main():
    rev = Reverse('Spam')
    iter(rev)
    for char in rev:
        print(char)
    pass


if __name__ == '__main__':
    main()
    pass
