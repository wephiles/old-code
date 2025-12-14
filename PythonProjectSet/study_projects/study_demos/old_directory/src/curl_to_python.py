# -*- coding: utf-8 -*-
# @CreateTime : 2024/7/11 011 17:47
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : study_demos
# @FileName : study_demos/curl_to_python.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

# import requests
# 
# headers = {
#     'authority': 'oneapi.qmpoa.com',
#     'pragma': 'no-cache',
#     'cache-control': 'no-cache',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99"',
#     'dnt': '1',
#     'sec-ch-ua-mobile': '?0',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.310',
#     'sec-ch-ua-platform': '"Windows"',
#     'accept': '*/*',
#     'origin': 'https://www.qimingpian.com',
#     'sec-fetch-site': 'cross-site',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://www.qimingpian.com/',
#     'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
# }
# 
# data = {
#     'site': 'QMPCN',
# }
# 
# response = requests.post('https://oneapi.qmpoa.com/api/website/addWebsiteClick', headers=headers, data=data).json()
# 
# print(response)


import argparse

parser = argparse.ArgumentParser('创建parser对象')
parser.add_argument('--input', '-i', type=str)
parser.add_argument('--directory', '-d', type=str, default='./')
parser.add_argument('--file', '-f', type=str, default='test.txt')
parser.add_argument('--output', '-o', type=str, default='output.txt')

args = parser.parse_args()
input_name = args.input
file_name = args.file
output_name = args.output
directory_name = args.directory

print(input_name, file_name, output_name, directory_name)

# --END--
