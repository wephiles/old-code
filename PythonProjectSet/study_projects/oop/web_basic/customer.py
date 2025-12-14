#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2025/01/19 21:42
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/customer.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8080))
sock.listen(5)

while True:
    conn, addr = sock.accept()
    print('There is a connection, connection address is:', addr)

    # 连接成功后立即发送
    conn.sendall('欢迎使用XXX系统，请输入您要办理的业务:'.encode('utf-8'))

    while True:
        data = conn.recv(1024)

        if not data:
            break
        data_string = data.decode('utf-8')

        # 回复消息
        conn.sendall('你说啥？'.encode('utf-8'))
    print('用户已断开连接！')
    conn.close()

sock.close() 

# --END--
