# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/24 024 21:07
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/demo2.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

# class Foo(object):
#
#     def __init__(self, age):
#         self.age = age
#
#     def display(self):
#         print("age is:", self.age)
#
#
# data_list = [Foo(8), Foo(9)]
#
# for item in data_list:
#     print("年龄是:", item.age, )
#     print(item.display())


# class StartConfig(object):
#     def __init__(self, num):
#         self.num = num
#
#     def change_list(self, request):
#         print(self.num, request)
#
#
# class RoleConfig(StartConfig):
#
#     def change_list(self, request):
#         print(666)
#
#
# config_obj_list = [StartConfig(1), StartConfig(2), RoleConfig(3)]
# for item in config_obj_list:
#     print(item.num)


# class StartConfig(object):
#     def __init__(self, num):
#         self.num = num
#
#     def change_list(self, request):
#         print(self.num, request)
#
#
# class RoleConfig(StartConfig):
#
#     pass
#
#
# config_obj_list = [StartConfig(1), StartConfig(2), RoleConfig(3)]
# for item in config_obj_list:
#     print(item.change_list(168))

# class StartConfig(object):
#     def __init__(self, num):
#         self.num = num
#
#     def change_list(self, request):
#         print(self.num, request)
#
#
# class RoleConfig(StartConfig):
#
#     def change_list(self, request):
#         print(666, self.num)
#
#
# config_obj_list = [StartConfig(1), StartConfig(2), RoleConfig(3)]
# for item in config_obj_list:
#     print(item.change_list(168))

# class StartConfig(object):
#     def __init__(self, num):
#         self.num = num
#
#     def change_list(self, request):
#         print(self.num, request)
#
#     def run(self):
#         self.change_list(999)
#
#
# class RoleConfig(StartConfig):
#
#     def change_list(self, request):
#         print(666, self.num)
#
#
# config_obj_list = [StartConfig(1), StartConfig(2), RoleConfig(3)]
# for item in config_obj_list:
#     item.run()

# class UserInfo(object):
#     pass
#
# class Department(object):
#     pass
#
# class StartConfig(object):
#     def __init__(self, num):
#         self.num = num
#
#     def change_list(self, request):
#         print(self.num, request)
#
#     def run(self):
#         self.change_list(999)
#
#
# class RoleConfig(StartConfig):
#
#     def change_list(self, request):
#         print(666, self.num)
#
#
# class AdminSite(object):
#     def __init__(self):
#         self._registry = dict()
#
#     def register(self, k, v):
#         self._registry[k] = v(k)
#
#
# # config_obj_list = [StartConfig(1), StartConfig(2), RoleConfig(3)]
# # for item in config_obj_list:
# #     item.run()
#
# site = AdminSite()
#
# site.register(UserInfo, StartConfig)
# site.register(Department, StartConfig)
#
# for k, row in site._registry.items():
#     # {UserInfo: StartConfig(UserInfo), Department: StartConfig(Department)}
#     row.run()


# class Base(object):
#
#     def f1(self):
#         print("Base.f1, 实现三个功能")
#
#
# class Foo(Base):
#
#     def f1(self):
#         print("Foo.f1, 实现五个功能")
#         Base.f1(self)  # 主动调用
#
#
# # 如果要执行八个功能 如上
# obj = Foo()
# obj.f1()


# class Base(object):
#
#     def f1(self):
#         print("Base.f1, 实现三个功能")
#
#
# class Foo(Base):
#
#     def f1(self):
#         print("Foo.f1, 实现五个功能")
#         super().f1()  # 按照类的继承顺序去找
#
#
# # 如果要执行八个功能 如上
# obj = Foo()
# obj.f1()


# class Base(object):
#
#     def f1(self):
#         print("Base.f1, 实现三个功能")
#
#
# class Foo(object):
#
#     def f1(self):
#         super().f1()  # self传进来的是哪个对象-就按照哪个对象的继承顺序去找下一个 找下一个！！！ 是找下一个！！！
#         print("Foo.f1, 实现五个功能")
#
#
# class Bar(object):
#     def f1(self):
#         print("Base.f1, 实现六个功能！")
#
#
# class Info(Foo, Bar):
#     pass
#
#
# # 如果要执行八个功能 如上
# obj = Foo()
# obj.f1()


class Foo(object):

    def __new__(cls, *args, **kwargs):
        """
        创建一个空的对象，然后返回这个对象，在__init__方法中进行初始化
        必须设置返回值，否则执行完__new__后不会自动执行__init__方法 并且，返回值必须是object.__new__(cls)
        Args:
            *args ():
            **kwargs ():
        """
        # 那么问题来了，这个v1和obj = Foo(1, 2) 是不是同一个对象？
        # 答案是：内存地址是一样的，但是里面的值是不一样的，因为object.__new__(cls)是空的 但是v1是真正有值的对象 -- 内存地址是一样的
        return object.__new__(cls)  # python内部创建一个当前类的对象(初始时内部是空的) 在__init__里面才进行初始化，使变得不空

    def __init__(self, a1, a2):
        """
        为空对象进行数据初始化。
        Args:
            a1 ():
            a2 ():
        """
        self.a1 = a1
        self.a2 = a2

    def __call__(self, *args, **kwargs):
        """

        Args:
            *args ():
            **kwargs ():

        Returns:

        """
        print(1111, args, kwargs)
        return 123

    def __getitem__(self, item):
        """

        Args:
            item ():

        Returns:

        """
        print(item)
        return 8

    def __setitem__(self, key, value):
        """
        这种的是没有返回值的。
        Args:
            key ():
            value ():

        Returns:

        """

        print(key, value, 123)

    def __delitem__(self, key):
        """
        这种的是没有返回值的。
        Args:
            key ():
        Returns:

        """
        print(key)

    def __add__(self, other):
        """

        Args:
            other ():

        Returns:

        """
        return self.a1 + other.a1

    def __enter__(self):
        """

        Returns:

        """
        print(111)
        return 132456

    def __exit__(self, exc_type, exc_val, exc_tb):
        """

        Args:
            exc_type ():
            exc_val ():
            exc_tb ():

        Returns:

        """
        print(222)


# 类名() 自动执行__init__方法
obj = Foo(1, 2)

# 对象() 自动执行__call__方法
res = obj(1, 2, 3, k1=1, k2=2)
print(res)

# 对象[] 自动执行__getitem__方法
res = obj['yu']
print(res)

# 对象[xxxx] = xxx 自动执行__setitem__方法
obj["computer"] = "science"

# del 对象[xxx] 自动执行__delitem__方法
del obj["xxx"]

# 还有很多的方法 自己查看源码


# 对象 + 对象 自动执行__add__方法
obj1 = Foo(1, 2)
obj2 = Foo(3, 4)

res = obj1 + obj2  # 这里会报错 因为没有实现__add__方法
print(res)

# with 对象.方法 自动执行__enter__方法
with obj as f:
    print("内部的代码！")
    print(f)  # 这个f就是__enter__方法的返回值

# 真正的构造方法  __new__ 在实例化对象的时候，先执行__new__方法 再执行__init__方法


# 对象 * 对象 自动执行__mul__方法
# 对象 in 对象 自动执行__contains__方法
# 对象 == 对象 自动执行__eq__方法
# 对象 != 对象 自动执行__ne__方法
# 对象 < 对象 自动执行__lt__方法
# 对象 <= 对象 自动执行__le__方法
# 对象 > 对象 自动执行__gt__方法
# 对象 >= 对象 自动执行__ge__方法
# 对象 | 对象 自动执行__or__方法
# 对象 & 对象 自动执行__and__方法
# 对象 ^ 对象 自动执行__xor__方法
# 对象 << 对象 自动执行__lshift__方法
# 对象 >> 对象 自动执行__rshift__方法
# 对象 ** 对象 自动执行__pow__方法
# 对象 // 对象 自动执行__floordiv__方法
# 对象 / 对象 自动执行__truediv__方法
# 对象 % 对象 自动执行__mod__方法
# 对象() 自动执行__call__方法
# 对象[xxx] 自动执行__getitem__方法
# 对象[xxx] = xxx 自动执行__setitem__方法
# del 对象[xxx] 自动执行__delitem__方法
# 对象 += 对象 自动执行__iadd__方法
# 对象 *= 对象 自动执行__imul__方法
# 对象 |= 对象 自动执行__ior__方法
# 对象 &= 对象 自动执行__iand__方法
# 对象 ^= 对象 自动执行__ixor__方法
# ...


# --END--
