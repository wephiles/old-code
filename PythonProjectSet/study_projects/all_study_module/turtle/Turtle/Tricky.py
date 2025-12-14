# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/9 22:15
# @Author : 20866
# @Site : 
# @Project: turtle
# @File : Tricky.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

from turtle import *


def main():
    hideturtle()
    penup()
    seth(90)
    fd(200)
    write('≧◠◡◠≦\n\n在你回答出来正确答案之前是关不掉滴。\n', align="left", font=("楷体", 15, "normal"))
    home()

    for i in range(0, 1000):
        x = textinput('智力测试', '你是不是傻，请回答"是"或者"否"')
        if x == '是':
            clear()
            write('对喽 \n有自知之明!≧◔◡◔≦', align="left", font=("楷体", 15, "normal"))
            delay(500)
            break
        elif x == '否':
            clear()
            write('(≧◉◡◉≦)你知道你最缺啥吗？\n\n(¬‿¬) 你最缺自知之明,\n\n(͡° ͜ʖ ͡°)请再次思考你的回答是否正确！', align="left", font=("楷体", 15, "normal"))
        else:
            clear()
            write('亲，请输入"是"或者"否"\n您的回答让我觉得您智力欠佳！', align="left", font=("楷体", 15, "normal"))
            seth(270)
            fd(60)
            write('☹', align="left", font=("楷体", 60, "normal"))
            bk(60)
    done()


if __name__ == '__main__':
    main()















