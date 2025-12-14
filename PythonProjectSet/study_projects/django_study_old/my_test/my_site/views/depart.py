# -*- coding: utf-8 -*-
# @CreateTime : 2023/5/18 018 21:08
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/depart.py
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

def depart_list(request, ):
    """
    部门列表展示。

    Parameters
    ----------
    request

    Returns
    -------
    render object
    """

    # 获取部门列表
    query_set = models.Department.objects.all()

    # 分页：
    page_object = Pagination(request, query_set, page_size=2)
    context = {
        "queryset": page_object.page_query_set,
        "page_string": page_object.html(),
    }
    return render(request, 'depart_list.html', context)
    # return render(request, 'depart_list.html', {'queryset': query_set})


def depart_add(request, ):
    """
    添加部门。

    Parameters
    ----------
    request

    Returns
    -------
    render object
    """
    if request.method == 'GET':
        # 添加部门
        return render(request, "department_add.html")
    # 获取提交过来的数据 (需要判断输入为空，此处先不做判断)
    title = request.POST.get("title")
    # 保存到数据库
    models.Department.objects.create(title=title)
    # 重定向回页面
    return redirect('/depart/list/')


def depart_delete(request, ):
    """
    删除部门。

    Parameters
    ----------
    request

    Returns
    -------
    render object
    """
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect('/depart/list/')


def depart_edit(request, nid: int, ):
    """
    编辑部门。

    Parameters
    ----------
    nid
    request

    Returns
    -------
    render object
    """
    if request.method == 'GET':
        # 根据nid，获取他的数据
        row_object = models.Department.objects.filter(id=nid).first()
        # print(row_object.id, row_object.title)
        return render(request, 'depart_edit.html', {'rowobject': row_object})
    # 拿到标题
    title = request.POST.get('title')

    # 根据ID找到并更新数据
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect('/depart/list/')

# END
