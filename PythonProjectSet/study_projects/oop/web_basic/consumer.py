#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2025/01/19 21:43
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/consumer.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
# client.connect(('localhost', 8080))

message = client.recv(1024)
print(message.decode('utf-8'))

while True:
    content = input('Me(                             q/Q to quit!) >>> ')
    if content == 'q' or 'Q':
        break
    client.sendall(content.encode('utf-8'))

    reply = client.recv(1024)
    print('Customer >>> ', reply.decode('utf-8'))

client.close()

# --END--
