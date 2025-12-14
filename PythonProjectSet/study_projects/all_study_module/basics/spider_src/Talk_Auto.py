# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/1 17:05
# @Author : 20866
# @Site : 
# @Project: Pycharm_Project_Set
# @File : Talk_Auto.py
# @Software : PyCharm

# This is a little program that can talk with you !

import requests
import json


def main():
    while True:
        # Receive the information which the users input :
        user_input = input('Please enter what you want to say:')
        # Establish a network connection：<Response [200]>
        # Get the data returned by the interface：、
        text = requests.get('http://api.qingyunke.com/api.php?key=free&appid=0&msg='+user_input+'').text
        # Parse JSON data
        # Load data into JSON parsing tool --> Dictionary
        result = json.loads(text)
        # Retrieve data
        print('Robot：'+result['content'])


if __name__ == '__main__':
    main()

















