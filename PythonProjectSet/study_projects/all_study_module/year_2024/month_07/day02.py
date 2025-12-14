# -*- coding: utf-8 -*-
# @CreateTime : 2024/7/2 002 16:57
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : all_study_module
# @FileName : all_study_module/day02.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import time
from indently import retry


@retry(retries=3, delay=1)
def connect() -> None:
    time.sleep(1)
    raise Exception('Could not connect to internet...')


def main() -> None:
    connect()

# --END--
