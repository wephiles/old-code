# -*- coding: utf-8 -*-
# @CreateTime : 2024/1/27 027 22:07
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/demo01.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles


def main() -> int:
    # info = {
    #     'name': 'computer',
    #     'age': 10,
    #     'status': True,
    #     'hobby': ['sing', 'dance', 'rap', 'basketball']
    # }
    # 
    # for item in info:
    #     print(item)

    # addr_list = [
    #     ["王*非", "北京市,海淀区", "北京市海淀区xxx"],
    #     ["李*龙", "上海市,浦东新区", "上海市浦东新区xxx"],
    #     ["卜*瑜", "北京市,顺义区", "当代北辰悦moma"]
    # ]
    #
    # for item in addr_list:
    #     addr = item[1].split(",")[0]
    #     print(addr)

    # addr_list = [
    #     ["王*非", "北京市,海淀区", "北京市海淀区xxx"],
    #     ["李*龙", "上海市,浦东新区", "上海市浦东新区xxx"],
    #     ["卜*瑜", "北京市,顺义区", "当代北辰悦moma"],
    #     ["赵*雪", "江苏省,苏州区", "苏州大学"]
    # ]
    # info = {}
    # for item in addr_list:
    #     name = item[0]
    #     city = item[1].split(",")[0]
    #     if city not in info:
    #         info[city] = []
    #         info[city].append(name)
    #     else:
    #         info[city].append(name)
    # print(info)

    # addr_list = [
    #     ["王*非", "北京市,海淀区", "北京市海淀区xxx"],
    #     ["李*龙", "上海市,浦东新区", "上海市浦东新区xxx"],
    #     ["卜*瑜", "北京市,顺义区", "当代北辰悦moma"],
    #     ["赵*雪", "江苏省,苏州区", "苏州大学"]
    # ]
    #
    # info = {}
    # for item in addr_list:
    #     name = item[0]
    #     city = item[1].split(",")[0]
    #     if city not in info:
    #         info[city] = []
    #         info[city].append(name)
    #     else:
    #         info[city].append(name)
    # print(info)

    # v1 = {11, 22, 33, 44}
    # v2 = {11, 22, 55, 66}
    #
    # # 方式1
    # v3 = v1.intersection(v2)
    # print(v3)  # {11, 22}
    #
    # # 方式2
    # v4 = v1 & v2
    # print(v4)

    # v1 = {11, 22, 33, 44}
    # v2 = {11, 22, 55, 66}
    #
    # # 方式1
    # v3 = v1.union(v2)
    # print(v3)  # {11, 22}
    #
    # # 方式2
    # v4 = v1 | v2
    # print(v4)

    # v1 = {11, 22, 33, 44}
    # v2 = {11, 22, 55, 66}
    #
    # # v1里面有 v2里面没有
    # s1 = v1.difference(v2)  # v1中有但v2中没有的值
    # s2 = v1 - v2
    # print(s1)
    # print(s2)

    # v1 = {11, 22, 33, 44}
    #
    # data = len(v1)
    # print(data)

    # v1 = {11, 22, 33, 44}
    #
    # for item in v1:
    #     print(item)

    # v1 = 0.1
    # v2 = 0.2
    #
    # print(v1 + v2)

    # v1 = 0.3
    # v2 = 0.2
    #
    # print(v1 + v2)

    # import decimal
    # v1 = decimal.Decimal("0.1")
    # v2 = decimal.Decimal("0.2")
    # print(v1 + v2)

    # name = "计算机"  # str字符串，底层是unicode编码
    # data = name.encode("utf-8")  # bytes字节，底层是UTF-8编码
    #
    # print(data)
    #
    # name = "计算机"  # str字符串，底层是unicode编码
    # data = name.encode("gbk")  # bytes字节，底层是gbk编码
    #
    # print(data)

    # name = "计算机"  # str字符串，底层是unicode编码
    # data = name.encode("utf-8")  # bytes字节，底层是gbk编码
    # old = data.decode("utf-8")
    # print(old)  # b'\xbc\xc6\xcb\xe3\xbb\xfa'

    # # 打开文件
    # # -    "unicome.txt"     文件路径
    # # -    mode="wb"         以写文件的模式打开
    # file_object = open("unicome.txt", mode="wb")
    #
    # # 写内容
    # name = "计算机\n"  # unicode
    # file_object.write(name.encode("utf-8"))
    # file_object.write(name.encode("utf-8"))
    #
    # # 关闭文件
    # file_object.close()

    # with open("unicome.txt", mode="wb") as file_object:
    #     while True:
    #         user = input("username")
    #         if user.upper() == "Q":
    #             break
    #         pwd = input("password")
    #         line = "{} {}\n".format(user, pwd)
    #
    #         # 写到内存中的缓冲区 还没有写到硬盘 关闭后才会写到硬盘
    #         file_object.write(line.encode("utf-8"))
    #
    #         file_object.flush()  # 强制将内存中的数据写入到硬盘

    # with open("unicome.txt", mode="ab") as file_object:
    #     while True:
    #         user = input("username")
    #         if user.upper() == "Q":
    #             break
    #         pwd = input("password")
    #         line = "{} {}\n".format(user, pwd)
    #
    #         # 写到内存中的缓冲区 还没有写到硬盘 关闭后才会写到硬盘
    #         file_object.write(line.encode("utf-8"))
    #         # file_object.flush()  # 强制将内存中的数据写入到硬盘

    # file_object = open("unicome.txt", mode="rb")
    # data = file_object.read()  # 读取文件所有内容
    # print(data)
    # file_object.close()
    # # b'\xe5\x8d\x9c\xe4\xbc\x9f\xe4\xbb\x95 123\ngood 123456\n123 123456\n'
    #
    # data_string = data.decode("utf-8")
    # print(data_string)

    # file_object = open("unicome.txt", mode="rb")
    # data = file_object.read()  # 读取文件所有内容
    # # print(data)
    # #
    # # # b'\xe5\x8d\x9c\xe4\xbc\x9f\xe4\xbb\x95 123\ngood 123456\n123 123456\n'
    # #
    # data_string = data.decode("utf-8")
    # # print(data_string)
    #
    # row_list = data_string.strip().split("\n")
    # print(row_list)
    # file_object.close()

    file_object = open("unicome.txt", mode="rb")
    # line1 = file_object.readline()
    # print(line1)
    #
    # line2 = file_object.readline()
    # print(line2)
    for line in file_object:
        line_string = line.decode("utf-8").strip()
        print(line_string)

    file_object.close()
    return 1


if __name__ == '__main__':
    main()

# END
