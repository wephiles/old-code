# -*- coding: utf-8 -*-
# @CreateTime : 2024/5/20 020 17:05
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/客户端.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import socket

client = socket.socket()

client.connect(("192.168.0.101", 8002))

while True:
    name = input("请输入姓名>>> ")
    if name == 'exit':
        break
    # 转换成字节发过去
    client.send(name.encode("utf-8"))
    response = client.recv(1024)
    print(response.decode("utf-8"))
client.close()

# --END--
