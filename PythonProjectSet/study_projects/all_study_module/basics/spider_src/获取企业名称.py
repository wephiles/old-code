# -*- coding: utf-8 -*-
# @CreateTime : 2021/11/29 18:40
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : 获取企业名称.py
# @Software : PyCharm

import requests
import json
# from bs4 import BeautifulSoup


def main():
    #  批量获取不同企业的地址ID
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36'
    }
    id_list = []  # 存储企业ID
    all_data_list = []
    for page in (1, 6):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        json_ids = requests.post(url=url, headers=headers, data=data).json()  # 字典类型
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
        # print(id_list)
        # 获取企业详情数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id_id in id_list:
        data = {
            'id': id_id
        }
        detail_json = requests.post(url=post_url, headers=headers, data=data).json()
        # print(detail_json, '----------------ending---------------')
        all_data_list.append(detail_json)
    with open('all_data.json', 'w', encoding='utf-8') as fp:
        json.dump(all_data_list, fp=fp, ensure_ascii=False)
    print('数据爬取成功，已存入文件')


if __name__ == '__main__':
    main()

# END
