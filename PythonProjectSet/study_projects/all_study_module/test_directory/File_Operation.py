# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/3 21:40
# @Author : 20866
# @Site : 
# @Project: Learn_File
# @File : File_Operation.py
# @Software : PyCharm

import os
import sys
import re
import time


def main():
    # file_name = 'first.txt'
    # word = 'Hello world!'
    # with open(file_name, 'w', encoding='utf-8') as fp:
    #     fp.write(word)
    # fp.close()
    # file_open = open(file_name, 'a', encoding='utf-8')
    # file_open.write('你好！')
    # file_open.close()
    # if not os.path.exists('Hello'):
    #     os.mkdir('Hello')
    # with open('Hello/Hello.txt', 'w', encoding='utf-8') as fp:
    #     fp.write('你好，我是一个傻逼！！！')
    # with open(r'D:\\系统默认\\桌面\\你好.txt', 'w', encoding='utf-8') as f:
    #     f.write('你好啊!我是卜伟仕xixixixixi')
    # fp.close()
    # f.close()

    # print('hello world')
    # try:
    #     x = float(input('请输入一个数字: '))
    #     print(x)
    # except ValueError:
    #     print('您输入的不是数字，请再次尝试输入！')
    #
    # try:
    #     f = open('myfile.txt')
    #     s = f.readline()
    #     i = int(s.strip())
    # except OSError as err:
    #     print("OS error: {0}".format(err))
    # except ValueError:
    #     print("Could not convert data to an integer.")
    # except:
    #     print("Unexpected error:", sys.exc_info()[0])
    #     raise
    # x = 10
    # if x > 5:
    #     raise Exception('x不能大于5,x的值为{}'.format(x))
    # print('OK!')
    # raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是# Exception的子类）。
    # 如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的raise 语句就可以再次把它抛出。
    # try:
    #     raise NameError('HiThere')
    # except NameError:
    #     print('An exception flew by!')
    #     raise
    # x = 0
    # y = 0
    # begin = time.time()
    # a = 1
    # b = 2
    # t = a
    # a = b
    # b = t
    # # print(a, b)
    # for i in range(0, 10000):
    #     x += i * i
    # end = time.time()
    # print('1 ', end-begin)
    # begin1 = time.time()
    # a = 1
    # b = 2
    # a, b = b, a
    # # print(a, b)s
    # for i in range(0, 10000):
    #     y += i * i
    # end1 = time.time()
    # print('2 ', end1 - begin1)
    print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
    print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配


if __name__ == '__main__':
    main()
