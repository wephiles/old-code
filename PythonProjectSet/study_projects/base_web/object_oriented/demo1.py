# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/17 017 21:07
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/demo1.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

class Message:

    def send_email(self, to_email):
        msg = "给{}发送了一封邮件。".format(to_email)
        print(msg)

    def send_dingding(self, to_email):
        msg = "给{}发送了一封钉钉消息。".format(to)
        print(msg)

    def send_wechat(self, to_email):
        msg = "给{}发送了一封微信消息。".format(to)
        print(msg)


obj = Message()
obj.company = "这是个公司名"
obj.number = 100000

# --END--
