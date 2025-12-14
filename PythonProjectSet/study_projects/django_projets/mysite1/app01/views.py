from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    """

    Args:
        request (): 默认参数

    Returns:

    """
    return HttpResponse("欢迎使用")


def user_list(request):
    # 默认只会去app目录下面的templates目录下去寻找html文件 -- 根据app的注册顺序一个个找
    # 但是我们可以在配置文件中修改一些参数，那么就会去别的地方找
    return render(request, "user_list.html")


def user_add(request):
    return render(request, "user_add.html")

