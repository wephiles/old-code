# -*- coding: utf-8 -*-
# @CreateTime : 2024/5/1 001 17:46
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/服务端.py
# @Description : 自动回复示例
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

import socket

server = socket.socket()

server.bind(("192.168.0.101", 8002))

server.listen(5)

while True:
    conn, addr = server.accept()
    while True:
        # data是字节类型
        data = conn.recv(1024)
        if data == 'exit':
            print("关闭")
            break
        response = data + b' SB'
        conn.send(response)
    conn.close()

# --END--
