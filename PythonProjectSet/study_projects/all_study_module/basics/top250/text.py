# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/23 21:40
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : text.py
# @Software : PyCharm
# !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe

import test1
import mysql.connector


def main():
    # test1.change()
    # my_db = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     passwd="WarmDou_TS0807"
    # )
    # my_cursor = my_db.cursor()
    # my_cursor.execute("CREATE DATABASE runoob_db")
    # print('OK')
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="WarmDou_TS0807",
        database="runoob_db"
    )
    my_cursor = my_db.cursor()
    # my_cursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
    my_cursor.execute("SHOW TABLES")

    for x in my_cursor:
        print(x)
    my_cursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
    for x in my_cursor:
        print(x)


if __name__ == '__main__':
    main()




