#!/user/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2024/12/18 21:43
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/日志.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

import logging

file_1 = logging.FileHandler('log1.log', mode='w', encoding='utf-8')
fmt1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_1.setFormatter(fmt1)

logger1 = logging.Logger('logger1', level=logging.ERROR)
logger1.addHandler(file_1)

# 另外一个
file_2 = logging.FileHandler('log2.log', mode='w', encoding='utf-8')
fmt2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_2.setFormatter(fmt2)

logger2 = logging.Logger('logger2', level=logging.ERROR)
logger2.addHandler(file_2)

logger1.error('error 1')
logger2.error('error 2')

# --END--
