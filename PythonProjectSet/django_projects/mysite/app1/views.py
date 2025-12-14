from django.shortcuts import render, HttpResponse, redirect
import requests
import re
from app1 import models

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.310"
}


# Create your views here.


def index(request):
    # return HttpResponse("hello world")
    return render(request, "index_test.html")


def test_templates(request):
    name = "computer"
    roles = ["computer", "admin", "ceo"]
    user_info = {"username": "admin", "password": "123456", "email": "dwada@qq.com"}
    data_list = [{"username": "admin", "password": "654132", "email": "dwa@qq.com"},
                 {"username": "root", "password": "78945da", "email": "dadwa@qq.com"},
                 {"username": "heima", "password": "adasda", "email": "dsadefg@qq.com"}]

    the_dict = {"n1": name, "n2": roles, "n3": user_info, "n4": data_list}
    return render(request,
                  "test_templates.html",
                  the_dict)


def unicom_news(request):
    # 一些新闻
    start_url = "https://www.chinaunicom.com.cn/43/menu01/1/column05?pageNo="
    msg_list = list()
    for k in range(10):
        url = start_url + str(k)
        response_text = requests.get(url=url, headers=headers).text
        title_list = re.findall(r'<td width="1000" data-v-00a8aa21>(.+?)</td>', response_text)
        time_list = re.findall(r'<td align="right" width="200" class="time" data-v-00a8aa21>(.+?)</td>', response_text)
        print(title_list)
        print(time_list)
    return render(request, "news.html")


def something(request):
    # request是一个对象 封装了用户通过浏览器发来的所有请求相关的数据

    # 获取用户请求方式
    x = request.method

    # 在url上传递一些值：
    # .../?n1=123&n2=999
    n1 = request.GET.get("n1")
    n2 = request.GET.get("n2")

    # 如果发送的是post请求 (在请求体中提交数据) 获取对象
    print(request.POST)

    a_dict = {"x": x,
              "n1": n1,
              "n2": n2}
    # 响应
    # return render(request, "something.html", a_dict)
    # 响应 -- 重定向
    # return redirect("https://www.baidu.com")
    return redirect("/index/")


def user_login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("password")
    if username == "admin" and password == "123456":
        return redirect("/index")
    return render(request, "login.html", {"error_msg": "账号密码错误，检查账户密码重新登录"})


def user_add(request):
    return render(request, "")


def test_orm(request):
    # 测试ORM操作表中的数据
    # 新建
    # models.Department.objects.create(title="瑞克")
    # models.Department.objects.create(title="莫蒂")
    # models.Department.objects.create(title="桑美")
    # models.UserInfo.objects.create(name="computer", password="123456", age=18)
    # models.UserInfo.objects.create(name="science", password="123456", age=18)
    # models.UserInfo.objects.create(name="technology", password="123456", age=18)

    # # 删除
    # models.Department.objects.filter(id=3).delete()
    # models.Department.objects.all().delete()  # 删除所有表里面的数据
    # models.Department.objects.create(title="杰瑞")
    # models.Department.objects.create(title="格林")
    # models.UserInfo.objects.create(name="aaa", password="asdadasdw", age=25)
    # models.UserInfo.objects.create(name="bbb", password="465489654", age=15)
    # models.UserInfo.objects.create(name="ccc", password="123da4dadeasd56", age=58)

    # 获取数据

    # # 获取所有数据 返回的东西类似于列表 每一行都是一个对象
    # query_set = models.UserInfo.objects.all()
    # data_list = []
    # for obj in query_set:
    #     data_list.append((obj.id, obj.name, obj.password, obj.age, ))

    # # 获取某些信息
    # data = models.UserInfo.objects.filter(id=1).first()
    # # 就算只能查出一条数据 返回的也是一个对象列表只不过只有一条数据
    #
    # data_list = [[data.id, data.name, data.password, data.age]]

    # 更新
    models.UserInfo.objects.filter(id=3).update(password="999999")
    return HttpResponse("...")


def info_list(request):
    # 获取数据库中所有用户信息
    data_obj_list = models.UserInfo.objects.all()
    # param_list = list()
    # for item in data_obj_list:
    #     param_list.append((item.id, item.name, item.password, item.age))
    # data_dict = {'n1': param_list}
    return render(request, "info_list.html", {"data_list": data_obj_list})


def info_add(request):
    if request.method == "GET":
        return render(request, "user_add.html")
    name = request.POST.get("name")
    password = request.POST.get("password")
    age = request.POST.get("age")

    models.UserInfo.objects.create(name=name, password=password, age=age)
    return redirect("/info/list/")


def info_del(request):
    nid = request.GET.get('nid')
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/info/list")

# --END--
