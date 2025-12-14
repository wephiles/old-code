# -*- coding: utf-8 -*-
# @CreateTime : 2024/7/2 002 17:01
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : all_study_module
# @FileName : all_study_module/indently.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import time
from functools import wraps
from time import sleep
from typing import Callable, Any


def retry(retries: int = 3, delay: float = 1) -> Callable:
    """
    尝试去调用一个函数，如果失败了，在指定的延迟之后再次尝试。
    Args:
        retries ():
        delay ():

    Returns:

    """
    if retries < 1 or delay <= 0:
        raise ValueError('Are you high, mate?')

# --END--
