# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/29 029 17:17
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : all_study_module
# @FileName : all_study_module/print_list.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

"""
This module shows how to print a list which contains many depth of list.(Ok, my English is bad >_<, I am a chinese^_^.)
"""


def print_list(the_list: list):
    """
    This function prints a list which contains many depth of list.
    Args:
        the_list (list): A list.

    Returns:
        None
    """
    for item in the_list:
        if isinstance(item, list):
            print_list(item)
        else:
            print(item)

# --END--
