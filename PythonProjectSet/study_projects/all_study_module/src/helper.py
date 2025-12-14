#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime  :2024/09/04 20:18
# @Author      :wephiles@20866
# @IDE         :PyCharm
# @ProjectName :all_study_module
# @FileName    :all_study_module/helper.py
# @Description :This is description of this script.
# @Interpreter :Python 3.0+
# @Motto       :You must take your place in the circle of life!
# @AuthorSite  :https://github.com/wephiles or https://gitee.com/wephiles

import time


def get_time() -> str:
    """Gets the current time and returns it as a str.

    Returns:
        Example: '14:57:03 (28/01/24)'
    """
    return time.strftime("%X (%d/%m/%Y)")
# --END--
