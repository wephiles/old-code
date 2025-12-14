# -*- coding: utf-8 -*-
# @CreateTime : 2024/2/25 025 17:52
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/lambda_function.py
# @Description : lambda表达式 —— 匿名函数
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles


def main() -> int:
    # # func是函数名(变量)
    # # lambda: 函数体 --- 你写一个123，内部return一个123
    # func = lambda: 123
    #
    # res = func
    # print(res())  # 123
    # 注意：
    data_list = [11, 22, 33]

    res = data_list.append(44)
    print(res)
    return 0


if __name__ == "__main__":
    main()

# --END--
