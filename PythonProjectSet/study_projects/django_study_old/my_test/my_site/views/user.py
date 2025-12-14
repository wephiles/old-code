# -*- coding: utf-8 -*-
# @CreateTime : 2023/5/18 018 21:08
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/user.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles

from django.shortcuts import render, redirect
from my_site import models
# from django import forms
# from django.core.validators import RegexValidator
# from django.core.validators import ValidationError
# from django.utils.safestring import mark_safe
# from datetime import datetime
from my_site.utils.pagination import Pagination
from my_site.my_forms.form import PrettyNumberEditModelForm
from my_site.my_forms.form import UserModelForm, PrettyNumberModelForm

def user_list(request, ):
    """
    用户列表展示。

    Parameters
    ----------
    request

    Returns
    -------
    render object
    """

    # 获取所有用户列表
    query_set = models.UserInfo.objects.all()
    # for item in query_set:
    # print(item.id, item.age, item.name, item.create_time.strftime("%Y-%m-%d"), item.gender, item.password,
    #       item.account, item.depart_id)
    # 获得gender_choices = (
    #         (1, "男"),
    #         (2, "女"),
    #     )
    # 这种类型的数据，不只是获得简单的1 / 2
    # get_字段名_display() 如果写的是level_choices,那么就写get_level_display()

    # 此外，另外一张表通过外键关联到ID的时候，
    # depart = models.ForeignKey(to="Department", to_field="id", verbose_name="部门", on_delete=models.CASCADE)
    # 如何获取部门的值呢？直接通过item.depart.title 来获取文字， 而不是创建这一列的时候产生的ID (depart_id)

    # print(item.id, item.age, item.name, item.create_time.strftime("%Y-%m-%d"), item.get_gender_display(),
    #       item.password, item.account, item.depart.title)

    # 分页：
    page_object = Pagination(request, query_set, page_size=2)
    context = {
        "queryset": page_object.page_query_set,
        "page_string": page_object.html(),
    }
    return render(request, 'user_list.html', context)


def user_add(request, ):
    """
    添加用户（原始方式）。

    Parameters
    ----------
    request

    Returns
    -------
    render object
    """
    # if request.method == 'GET':
    #     # 添加用户
    #     return render(request, "user_add.html")
    context = {
        'genderchoices': models.UserInfo.gender_choices,
        'departlist': models.Department.objects.all(),
    }
    # 重定向回页面
    return render(request, 'user_add.html', context)


def user_model_form_add(request, ):
    """
    添加用户 —— 基于 ModelFormForm

    Parameters
    ----------
    request

    Returns
    -------

    """
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_model_form_add.html', {'form': form})

    # 用户post提交数据 数据校验
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 如果合法，保存到数据库
        form.save()
        return redirect('/user/list/')
        # print(form.cleaned_data)  # 校验成功
    else:
        # 在页面上显示错误信息
        return render(request, 'user_model_form_add.html', {'form': form})


def user_edit(request, nid: int):
    """
    编辑用户。

    Parameters
    ----------
    request

    Returns
    -------

    """

    # 根据ID获取要编辑的那一行数据(对象)
    # 自动获取所有的 row_object对象
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {'form': form})

    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 默认保存的是用户输入的所有数据
        form.save()

        # 想要用户输入以外增加一些值
        # form.instance.字段名 = 值
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {'form': form})


def user_delete(request, nid: int):
    """
    删除用户。

    Parameters
    ----------
    request
    nid

    Returns
    -------

    """
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")

# END
