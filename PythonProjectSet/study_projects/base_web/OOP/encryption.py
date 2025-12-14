# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/28 028 19:31
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/encryption.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

import hashlib

SALT = b"daojdjuioaejhwdejas98dfjoiwejf9pweqj9iJCOPIEJWFUOHREIUOFHJ9ERHJGUIEHGUHJDIS9UPHFGOISAJR8T9FHUEWSOUIGHOLIDFSUAH"

obj = hashlib.md5()  # 先实例化一个对象
obj.update("admin".encode("utf-8"))  # 想对谁加密，就把参数传进去 在python3.5中，这个参数必须是字节
v = obj.hexdigest()  # 获取密文
print(v)  # 21232f297a57a5a743894a0e4a801fc3

obj1 = hashlib.md5(SALT)  # 先实例化一个对象 这波加盐 防止撞库被发现密码 传一个盐进去 这个盐必须是字节码
obj1.update("admin".encode("utf-8"))  # 想对谁加密，就把参数传进去 在python3.5中，这个参数必须是字节码
v = obj1.hexdigest()  # 获取密文
print(v)  # 21232f297a57a5a743894a0e4a801fc3

# --END--
