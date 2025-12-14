#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2025/01/19 21:04
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/main.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

import socket
import time

# 监听本机的IP和端口
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind(('192.168.1.5', 8001))  # (IP, Port)
sock.bind(('127.0.0.1', 8001))  # (IP, Port) 此IP是本地环回地址
sock.listen(5)  # 支持排队等待五人

start_time = time.time()

while True:

    if time.time() - start_time > 20000:
        # 假设当发生某一事件我不想继续服务了就可跳出循环
        break

    # 等待，有人来连接（阻塞）
    conn, addr = sock.accept()  # 等待客户端来连接，如果没连接那么一直在阻塞，addr是向服务端发送连接请求的IP地址。
    # conn就是类似于一个连接的管道

    # 等待，连接者发送消息（阻塞）
    client_data = conn.recv(1024)  # 等待接受客户端发来的消息，如果不发那么一直阻塞
    print(client_data)  # 字节类型的数据
    print(client_data.decode('utf-8'))  # 转换成字符类型的数据

    # 给连接者回复消息
    conn.sendall(b'Hello, client!')

    # 关闭连接
    conn.close()

# 停止服务端程序
sock.close()

# --END--
