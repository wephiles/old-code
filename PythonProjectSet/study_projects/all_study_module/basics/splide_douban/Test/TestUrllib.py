# -*- codeing = utf-8 -*-
# @Time : 2021/5/31 9:18
# @Auther : 20866
# @Site : 
# @File : TestUrllib.py
# @Software : PyCharm
import urllib.request
import urllib.parse
### 1 通过get方式获取文件
# response = urllib.request.urlopen("http://www.baidu.com") ###通过urllib库中的request模块中的urllib函数打开一个网页
# print(response)
### <http.client.HTTPResponse object at 0x0000016708D22F70>
# print(response.read()) ###这个语句将网页源代码打印出来以后 发现有一部分文字是不可理解
# print(response.read().decode('utf-8')) ### .decode('utf-8') 是把网页源代码以utf-8方式解析 可以成功显示中文


### 1 通过post方式获取文件
### 专用测试网址： http://httpbin.org/

# data = bytes(urllib.parse.urlencode({"what?":"???"}),encoding = 'utf-8') ###将文件信息转换成二进制的文件 需要import urllib.parse
# response1 = urllib.request.urlopen('http://httpbin.org/post',data = data) ### 封装
# print(response1.read().decode('utf-8')) ### 在未封装之前 会出现405错误  urllib.error.HTTPError: HTTP Error 405: METHOD NOT ALLOWED
# ### 用post方法访问的时候 不能直接用post请求 需要进行封装

### 访问超时等情况及其处理

# try:
#     response2 = urllib.request.urlopen('http://httpbin.org/', timeout = 10)
#     print(response2.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out !")

### 解析网页
# response3 = urllib.request.urlopen('http://httpbin.org/')
# print(response3.status)
# ### 200 状态码

# response4 = urllib.request.urlopen('http://www.douban.com')
# print(response4.status) ### urllib.error.HTTPError: HTTP Error 418:  这个报错表示对方已经发现是爬虫 我是一个茶壶（梗）

# response5 = urllib.request.urlopen('http://www.baidu.com')
# print(response5.getheaders()) ###  百度网页 Response Headers 中的信息 一一对应 得到一个列表
# # print(response5.getheaders('Bdpagetype')) ### 有错误 因为getheaders方法中不能有一个参数 有一个参数的方法为 getheader
# print(response5.getheader('Bdpagetype'))


# url = "http://httpbin.org/post"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
#            }### 封装
# data = bytes(urllib.parse.urlencode({"name":"bws"}),encoding = 'utf-8')### 封装
# req = urllib.request.Request(url = url,data = data ,headers = headers,method = "POST") ####请求对象
# response = urllib.request.urlopen(req) ### 响应请求

# print(response)
### <http.client.HTTPResponse object at 0x000001EE92F72F10>

# print(response.read())
### 打印全在一行

# print(response.read().decode("utf-8"))
### 打印正常格式


url = "https://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
           }
req = urllib.request.Request(url = url ,headers = headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))







