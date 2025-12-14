# -*- coding: utf-8 -*-
# @CreateTime : 2023/5/18 018 21:08
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/number.py
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

def pretty_number_list(request):
    """

    Parameters
    ----------
    request

    Returns
    -------

    """

    data_dict = {}
    # 如果data_dict为空，则是找到所有的
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['mobile__contains'] = search_data
    # 用自己定义的组件类实现分页
    query_set = models.PrettyNumber.objects.filter(**data_dict)
    page_object = Pagination(request, query_set)
    page_query_set = page_object.page_query_set
    page_string = page_object.html()
    context = {
        'queryset': page_query_set,  # 分完页的数据
        'search_data': search_data,
        'page_string': page_string,  # 页码
    }
    return render(request,
                  "pretty_number_list.html",
                  context)


def pretty_number_add(request, ):
    """
    添加靓号

    Parameters
    ----------
    request

    Returns
    -------

    """
    if request.method == "GET":
        form = PrettyNumberModelForm()
        return render(request, 'pretty_number_add.html', {'form': form})
    form = PrettyNumberModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/pretty/number/list/')
    return render(request, 'pretty_number_add.html', {'form': form})


def pretty_number_edit(request, nid: int):
    """
    编辑靓号

    Parameters
    ----------
    request
    nid

    Returns
    -------

    """
    row_object = models.PrettyNumber.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = PrettyNumberEditModelForm(instance=row_object)
        return render(request, 'pretty_number_edit.html', {'form': form})

    # 将修改了的信息上传到数据库，而不是新建
    form = PrettyNumberEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 默认保存的是用户输入的所有数据
        form.save()

        # 想要用户输入以外增加一些值的话
        # form.instance.字段名 = 值
        return redirect('/pretty/number/list/')
    return render(request, 'pretty_number_edit.html', {'form': form})


def pretty_number_delete(request, nid):
    models.PrettyNumber.objects.filter(id=nid).delete()
    return redirect('/pretty/number/list/')

# END
