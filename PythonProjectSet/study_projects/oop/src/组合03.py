#!/user/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2024/12/08 15:13
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/组合03.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

class UserInfo(object):
    pass


class Department(object):
    pass


class StarkConfig(object):

    def __init__(self, num):
        self.num = num

    def change(self, request):
        print(self.num, request)

    def run(self):
        self.change(999)


class RowConfig(StarkConfig):
    def change(self, request):
        print(666, self.num)


class AdminSite(object):

    def __init__(self):
        self._registry = dict()

    def register(self, k, v):
        self._registry[k] = v(k)


site = AdminSite()

site.register(UserInfo, StarkConfig)
site.register(Department, StarkConfig)

for _, row in site._registry.items():
    row.run()

"""
<class '__main__.UserInfo'> 999
<class '__main__.Department'> 999
"""
# --END--
