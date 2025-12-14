# -*- coding: utf-8 -*-
# @CreateTime : 2024/7/11 011 18:00
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : study_demos
# @FileName : study_demos/run.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

"""
整个项目的入口
所有的测试都要在这个项目里面实现。
"""

import argparse


def main() -> int:
    parser = argparse.ArgumentParser('创建parser对象')
    parser.add_argument('--input', '-i', type=str)
    parser.add_argument('--directory', '-d', type=str, default='./')
    parser.add_argument('--file', '-f', type=str, default='test.txt')
    parser.add_argument('--output', '-o', type=str, default='output.txt')

    args = parser.parse_args()
    input_name = args.input
    file_name = args.file
    output_name = args.output
    directory_name = args.directory
    print()
    return 0


if __name__ == '__main__':
    main()

# --END--
