# -*- coding: utf-8 -*-
# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# @Author : 20866
# @CreateTime : 2022/4/8 10:32:56
# @Project: Pycharm_Project_Set
# @File : send_email.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

def check(word):
    if word[2] != word[5]:
        return False
    if word[3] != word[4]:
        return False
    word = str(int(word) + 1)
    if word[1] != word[5]:
        return False
    if word[2] != word[4]:
        return False
    word = str(int(word) + 1)
    if word[1] != word[4]:
        return False
    if word[2] != word[3]:
        return False
    word = str(int(word) + 1)
    if word[0] != word[5]:
        return False
    if word[1] != word[4]:
        return False
    if word[2] != word[3]:
        return False
    return True


def check_all():
    i = 100000
    while i <= 999996:
        if check(str(i)):
            print(i)
        i += 1


print('满足要求的示数是:')
check_all()

# END
