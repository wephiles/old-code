#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2025/01/19 21:23
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/client.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

import socket

# 向指定IP发送连接请求
client = socket.socket()
# client.connect(('192.168.1.5', 8001))
client.connect(('127.0.0.1', 8001))

# 连接成功后，发送消息
client.send(b'GET / HTTP/1.0\r\n\r\nhello!')

# 等待 消息的回复（阻塞）
reply = client.recv(1024)
print(reply)
print(reply.decode('utf-8'))

# 关闭连接
client.close()

# --END--
