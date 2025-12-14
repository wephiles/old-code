# -*- coding: utf-8 -*-
# @CreateTime : 2024/5/1 001 17:25
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/client.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles


import socket

# 创建一个socket对象

client = socket.socket()

# 向服务端发起链接请求 --传递链接介质(服务端接受，并命名为conn)
# 这个也是阻塞的 等链接成功后才会继续向下走
client.connect(("192.168.0.101", 8000))

input(">>> ")
client.send(b"hello")

# 等待服务端消息
data = client.recv(1024)
print(data)

client.close()

# --END--
