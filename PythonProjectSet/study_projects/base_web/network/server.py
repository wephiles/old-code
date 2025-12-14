# -*- coding: utf-8 -*-
# @CreateTime : 2024/5/1 001 16:07
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/server.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

import socket

# 创建一个socket对象
server = socket.socket()

# 绑定IP和端口
server.bind(("192.168.0.101", 8000))

# 服务端 监听连接 后面最多可以等5个连接
server.listen(5)

print("服务端准备开始接受客户端的连接")
# 等待客户端链接 如果没有客户端链接 则会阻塞，一直等
# 只有有客户端链接的时候 则获取客户端链接,然后开始进行通信
# conn是客户端和服务端的连接对象，服务端以后要通过这个对象来接收和发送数据
# addr是客户端的地址信息
conn, addr = server.accept()  # res1 是一个元组 (客户端的socket对象, 客户端的地址)
print("有人已经链接上了", conn, addr)

# 通过对象去获取客户端通过介质发送的数据时，最多一次性最多拿1024个字节
data = conn.recv(1024)
print("有人发来消息了:", data)

conn.send(b"stop")  # 通过链接对象去发送数据 给客户端发送字节数据

# 与客户端断开连接
conn.close()  # 关闭连接

# 关闭服务端的服务
server.close()  # 关闭服务端

# --END--
