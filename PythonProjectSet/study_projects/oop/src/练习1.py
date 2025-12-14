#!/user/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2024/12/17 19:54
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/练习1.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

class Operate(object):
    func_list = [
        'login', 'logout', 'register'
    ]

    def login(self):
        print('login')

    def logout(self):
        print('logout')

    def register(self):
        print('register')

    def run(self):
        print('''
        请输入要执行的功能:
        1. 登录
        2. 注销
        3. 注册
        ''')
        in_val = input('请输入要执行的操作序号1/2/3 >>> ')
        fun_str = self.func_list[int(in_val) - 1]
        getattr(self, fun_str)()


obj = Operate()
obj.run()

# --END--
