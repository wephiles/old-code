from django.shortcuts import render, HttpResponse, redirect
import requests
from lxml import etree
from app01.models import UserInfo, Department
# Create your views here.


def index(request):
    # 去注册的app的目录下去寻找，根据app注册的顺序逐一去app的templates中去寻找
    # 默认只会在app下去寻找，但是如果在setting.py中的 "DIRS": [os.path.join(BASE_DIR, 'templates')]加入的话
    # 默认先去项目目录下的templates里面去寻找 再在app下的目录中寻找 -- 要提前配置哦
    return render(request, 'index.html')


def user_list(request):
    return render(request, 'user_list.html')


def add_user(request):
    return render(request, 'add_user.html')


def tpl(request):
    name = 'denghaoliang'
    roles = ['admin', 'CEO', 'stuff']
    user_info = {'name': 'bu', 'salary': 10000, 'roles': 'CTO'}
    data_list = [{'name': 'deng', 'salary': 10000, 'roles': 'CEO'},
                 {'name': 'zhou', 'salary': 10000, 'roles': 'CEO'},
                 {'name': 'li', 'salary': 10000, 'roles': 'CTO'}]
    return render(request,
                  'tpl.html',
                  {"n1": name, "n2": roles, "n3": user_info, "n4": data_list})


def news(request):
    # 定义一些新闻 构造乘字典或者列表
    # 去数据库中寻找
    # 通过爬虫寻找新闻
    # url = 'http://www.chinaunicom.com.cn/news/list202304.html'
    url = 'http://www.chinaunicom.com.cn/news/list202304.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.301"
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = "utf-8"
    page_test = response.text

    tree = etree.HTML(page_test)
    divs = tree.xpath('//div[@id="page1"]/div[@class="item"]')

    title_time = {}
    title_time_list = []
    for div in divs:
        title = div.xpath('./div[@class="text"]/h2/a/text()')
        title_time["title"] = title[0]
        time = div.xpath('./div[@class="text"]/h2/span[@class="date"]/text()')
        title_time["time"] = time[0]
        title_time_list.append(title_time)
    return render(request,
                  "news.html",
                  {"n1": title_time_list})


def something(request):
    # request是一个对象   封装了发过来的所有请求

    # 1. 获取请求方式 get/post
    print(request.method)

    # 2. 在url上传递消息
    print(request.GET)

    # 在请求体中提交数据
    print(request.POST)

    # [响应] 内容字符串内容返回给请求者
    # return HttpResponse('返回内容')

    # 【响应】浏览器重定向
    # 发给Django后，Django向浏览器返回一个值 告诉浏览器自己去百度访问。
    # 而不是Django访问百度后向浏览器返回响应
    return redirect('https://www.baidu.com')
    # [响应] 读取HTML文档的内容 渲染+替换 ->字符串 返回给浏览器
    # return render(request, "something.html")


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    # post 请求 获取用户提交的数据
    if request.POST.get('user') == '123456@qq.com' and request.POST.get('pwd') == '123456':
        return HttpResponse('发送成功')
    return render(request, 'login.html', {"error_message": "用户名或密码错误"})


def orm(request):
    # 测试ORM操作表中的数据
    # return render(request, "")
    # Department.objects.create(title="销售部")
    # Department.objects.create(title="运营部")
    # Department.objects.create(title="IT部")
    # Department.objects.create(title="人事部")

    # UserInfo.objects.create(username="小明", password="m12345679", age=15)
    # UserInfo.objects.create(username="小泓", password="h12345679", age=16)
    # UserInfo.objects.create(username="小亮", password="l12345679", age=14)

    # # 删除数据：
    # for i in range(1, 14):
    #     # 加筛选条件
    #     UserInfo.objects.filter(id=i).delete()
    # # 删除一张表中所有记录：
    # UserInfo.objects.all().delete()
    # Department.objects.all().delete()

    # 获取所有数据 query_set = [行对象， 行对象， 行对象]
    # query_set = UserInfo.objects.all()
    # for obj in query_set:
    #     print(obj.username, obj.age, obj.password, end=' ')
    #     print('\n')

    # # 获取符合某些条件的数据 就算只有一个对象，依旧返回query set 对象
    # query_set = UserInfo.objects.filter(id=15)
    # for obj in query_set:
    #     print(obj.username, obj.age, obj.password, end=' ')
    #     print()

    # # 获取符合某些条件的数据 .first代表只去取一行数据 就算只有一个对象，依旧返回query set 对象
    # obj = UserInfo.objects.filter(id=15).first()
    # print(obj.username, obj.age, obj.password, end=' ')

    # 更新数据
    UserInfo.objects.all().update(password=999)

    return HttpResponse("成功")


def info_list(request):
    info_list = UserInfo.objects.all()  # 获取所有用户信息的对象
    return render(request, "user_info.html", {"n1": info_list})


def info_add(request):
    if request.method == 'GET':
        return render(request, 'info_add.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    age = request.POST.get('age')

    UserInfo.objects.create(username=username, password=password, age=age)
    # 添加成功后自动跳转
    # return HttpResponse("<h1>添加成功！</h1>")
    return redirect('/info/list/')


def info_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect('/info/list/')

# END
