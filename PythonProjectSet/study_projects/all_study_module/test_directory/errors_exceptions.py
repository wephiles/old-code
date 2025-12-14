# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/1/22 11:38:12
# @Project: Pycharm_Project_Set
# @File : errors_exceptions.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

# 类方法 ： 在方法上一行加一个 @classmethod 装饰器 cls参数就类似于self传入，
# 于是 cls()就相当于是这个类 详情见 https://www.cnblogs.com/king-lps/p/12597680.html
# 实例方法和类方法具体调用看：text.txt

#
# class People(object):
#     # 如果同样的属性名称同时出现在实例和类中，则属性查找会优先选择实例
#     name = 'Jerry'  # 所有实例都可以对其进行操作，共享
#     # 静态变量 可以被静态方法和类方法调用 所有实例共享的类变量
#
#
#     # 构造方法
#     def __init__(self, b, c):
#         # 实例变量 静态方法和类方法不能调用
#         # 每个实例唯一的实例变量 每个实例有每个实例的对实例变量的操作
#         self.b = b
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


# class B(Exception):
#     pass
#
#
# class C(B):
#     pass
#
#
# class D(C):
#     pass

def func():
    raise IOError


def main() -> None:
    # raise ValueError
    # raise ValueError(9)
    # 如果只想判断是否触发了异常，但并不打算处理该异常，则可以使用更简单的 raise 语句重新触发异常：
    # try:
    #     raise NameError('Hello!')
    # except NameError :
    #     print('An exception flew by!')
    #     raise
    try:
        func()
    except IOError as exc:
        raise RuntimeError('Failed to open database!') from exc
    pass


if __name__ == '__main__':
    # for cls in [B, C, D]:
    #     try:
    #         raise cls()
    #     except D:
    #         print('D')
    #     except C:
    #         print('C')
    #     except B:
    #         print('B')

    # x = People(1, 2)
    # x.write()  # 实例方法
    #
    # People.eat(10)  # 静态方法
    #
    # People.speak(4, 5)  # 类方法
    # x.speak(6, 7)  # 类方法
    main()
    pass
