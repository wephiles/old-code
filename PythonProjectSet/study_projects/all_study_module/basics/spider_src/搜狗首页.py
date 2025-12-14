# -*- coding: utf-8 -*-
# @CreateTime : 2021/11/28 20:19
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : 搜狗首页.py
# @Software : PyCharm

# 接下来就是激动人心的爬虫了!

# 需求：爬取搜狗首页的页面数据
import requests
from bs4 import BeautifulSoup


# 主函数
def main():
    # step_1 :指定url 以字符串的形式
    url = r'https://www.sogou.com/'
    # step_2 :发起请求

    # 用response接受get方法获得的网页返回值 get会返回一个响应对象 #
    # 这个响应对象针对get方法所获得的响应请求
    response = requests.get(url=url)
    # step_3 :获取响应数据 text返回的是字符串数据类型的返回数据
    page_text = response.text
    x = BeautifulSoup(page_text, 'lxml')
    print(x.prettify())
    # step_4 :持久化存储：存page_text(响应数据)
    with open('sought.html', 'w', encoding='utf-8') as fp:
        fp.write(x.prettify())
    print('爬取数据结束')


if __name__ == '__main__':
    main()

# END
