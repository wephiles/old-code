# -*- coding: utf-8 -*-
# @CreateTime : 2023/5/30 030 20:11
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/encrypt.py
# @Description : MD5 encryption
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles

import hashlib
from django.conf import settings


def md5(date_string):
    # 加盐，让MD5动起来，但是我们不用，哎嘿，就是玩儿——其实就是在settings里面加盐
    # salt = '卜伟仕是宇宙无敌超级大帅哥'
    # obj = hashlib.md5(salt.encode('utf-8'))

    # 我们用settings.py里面的SECRET_KEY
    salt = settings.SECRET_KEY
    obj = hashlib.md5(salt.encode('utf-8'))  # 加盐，让MD5动起来，但是我们不用，哎嘿，就是玩儿
    obj.update(date_string.encode('utf-8'))
    return obj.hexdigest()

# END
