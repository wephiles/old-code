'''
Created on 2021年5月10日

@author: 20866
'''

# 水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身


###判断一个数是不是水仙花数的方法

# def Judge_Num(Num):
#     Num_Record = Num
#     Add_Num = 0 
#     if Num >= 1000 or Num < 100 :
#         print(str(Num) + "不符合要求!")  ### 水仙花数是三位数 不是三位数的不符合要求
#     else:
#         while Num != 0:
#             a = Num % 10 
#             Add_Num += pow(a,3)
#             b = Num // 10 
#             Num = b
#         if Add_Num == Num_Record:
#             print(Add_Num)
# print("所有三位数中的水仙花数如下所示:")  
# 
# # for i in range(100,1000):
# #     if Judge_Num(i):
# #         print(i)   
# 
# for i in range(100,1000):
#     Judge_Num(i)



# import requests
# #jingdong = requests.get('https://img14.360buyimg.com/n1/s546x546_jfs/t493/221/135501307/78147/c78c3aeb/5451d0e6N85492051.jpg')
# #jingdong = requests.get('http://www.baidu.com')
# #jingdong = requests.get('http://dushu.baidu.com/api/pc/getChapterContent?data={%22book_id%22:%224315647161%22,%22cid%22:%224315647161|10221391%22,%22need_bookinfo%22:1}')
# # jingdong = requests.get('https://wenku.baidu.com/view/9e08e1ad1a37f111f1855b7c.html')
# jingdong = requests.get('https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=43139143227&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1')
# # jingdong = requests.get('')
# # jingdong = requests.get('')
# # jingdong = requests.get('')
# # jingdong = requests.get('')
# # jingdong = requests.get('')
# # jingdong = requests.get('')
# # jingdong = requests.get('')
# # jingdong = requests.get('')
# # jingdong = requests.get('')
# # jingdong = requests.get('')
# # jingdong = requests.get('')
# # jingdong = requests.get('')
# # jingdong = requests.get('')
# # jingdong = requests.get('')
# # jingdong = requests.get('')
# # jingdong = requests.get('')
# # jingdong = requests.get('')
# # jingdong = requests.get('')
# # jingdong = requests.get('')
# print(jingdong.text)

# import requests
# import json
# import openpyxl
# 
# wk = openpyxl.Workbook()
# sheet = wk.create_sheet()
# 
# 
# resp = requests.get('https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=43139143227&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1')
# content = resp.text
# rest = content.replace("fetchJSON_comment98(" , "").replace(");","")
# json_date = json.loads(rest)
# comments = json_date['comments']
# for item in comments:
#     color = item['productColor']
#     size = item['productSize']
#     sheet.append([color,size])
#     wk.save('data/BWS-18822321558.xlsx')
# ###ftp://47.92.3.25/
#
# import urllib.request
#
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response)
# print(response.read())
















