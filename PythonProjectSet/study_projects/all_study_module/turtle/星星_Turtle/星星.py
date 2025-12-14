#!/usr/bin/env python
# _*_coding:utf-8_*_
# @Time:2021/11/19 23:43
# @Author: 20866
# @Version: V3.9
# @File: 星星.py
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()