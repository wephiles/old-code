# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/15 015 12:23
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : requests_module
# @FileName : requests_module/demo8_xpath_test.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import requests
from bs4 import BeautifulSoup
from lxml import etree


def main():
    test_file_path = "./data/test.html"

    parser = etree.HTMLParser(encoding='utf-8')
    tree = etree.parse(test_file_path, parser=parser)

    # x = tree.xpath("/html/body/div")  # / 表示从根节点开始遍历 是一个Element对象
    # x = tree.xpath("/html//div")  # / 表示从根节点开始遍历 是一个Element对象 //表示多层级
    # x = tree.xpath("//div")  # //表示多层级 -- 从任意位置定位
    # x = tree.xpath("//div[@class='nav-primary']")  # //表示多层级 -- 从任意位置定位
    # x = tree.xpath("//div[@class='nav-primary']/div/a[2]")  # 索引从1开始

    # x = tree.xpath("//div[@class='nav-primary']/div/a[3]/text()")  # 索引从1开始 获取文本，获取的是一个列表
    # print(x)
    # print(x[0])

    # x = tree.xpath("//div[@class='nav-primary']/div/a[2]//text()")  # 索引从1开始 获取文本，获取的是一个列表
    # print(x)
    # print(x[0])

    # x = tree.xpath("//div[@class='nav-primary']/div/a[2]//text()")  # 索引从1开始 获取文本，获取的是一个列表
    # print(x)
    # print(x[0])
    # print(x[1])

    x = tree.xpath("//div[@class='nav-primary']/div/a[2]/@href")  # 索引从1开始 获取属性，获取的是一个列表
    print(x)
    print(x[0])


if __name__ == '__main__':
    main()

# --END--
