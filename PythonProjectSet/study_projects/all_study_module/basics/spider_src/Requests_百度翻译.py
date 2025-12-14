# -*- coding: utf-8 -*-
# @CreateTime : 2021/11/28 23:38
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : Requests_百度翻译.py
# @Software : PyCharm

# 破解百度翻译，找某一个单词或者某一个句子所对应的翻译结果

import requests
import json


def main():
    kw = input('Enter a wold:')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.107 Safari/537.36 HBPC/11.0.8.300'
    }
    # post 请求参数处理
    data = {
        'kw': kw
    }
    post_url = 'https://fanyi.baidu.com/sug'
    # post_url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
    response = requests.post(url=post_url, data=data, headers=headers)
    # page_text = response.text  # 返回字符串的json串
    dic_obj = response.json()  # 直接返回一个obj(对象) 如果确认服务器响应数据是json的，则可以用json返回
    print(dic_obj)
    file_name = kw+'.json'
    fp = open(file_name, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
    print('爬取数据结束')


if __name__ == '__main__':
    main()

# END
