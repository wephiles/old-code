# -*- coding: utf-8 -*-
# @CreateTime : 2024/08/09 19:44
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : study_pandas
# @FileName : study_pandas/quick_start.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

a: int = 10
b: int = 20


def add(a: int, b: int) -> int:
    return a + b


def main():
    x: int = add(10, 20)
    y: int = add(a, b)
    print(x, y)


if __name__ == '__main__':
    main()

# --END--
