# -*- coding: utf-8 -*-
# @CreateTime : 2024/2/25 025 18:38
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/ip_address_trans.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles


def main() -> int:
    ip_address = "192.168.11.23"
    a, b, c, d = ip_address.split(".")
    data_list = [a, b, c, d]
    bin_dict = []
    for item in data_list:
        bin_dict.append(bin(int(item)))
    bin_without_0b = []
    for item in bin_dict:
        bin_without_0b.append(item.replace("0b", ""))
    final_string = []
    for item in bin_without_0b:
        if len(item) != 8:
            final_string.append("0" * (8 - len(item)) + item)
        else:
            final_string.append(item)
    string = "".join(final_string)
    number = int(string, base=2)
    print(number)

    # 老师的
    ip = "192.168.11.23"
    bin_str_list = []
    str_list = ip.split(".")
    for item in str_list:
        bin_str = bin(int(item))[2:]
        bin_fill_str = bin_str.zfill(8)
        bin_str_list.append(bin_fill_str)
    num = int("".join(bin_str_list), base=2)
    print(num)
    return 0


if __name__ == "__main__":
    main()

# --END--
