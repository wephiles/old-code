# -*- coding: utf-8 -*-
# @CreateTime : 2024/7/2 002 16:16
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : all_study_module
# @FileName : all_study_module/module.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import time


def connect() -> None:
    print('Connecting to internet...')
    time.sleep(1)
    print('You are connected.')


if __name__ == '__main__':
    connect()

# --END--
