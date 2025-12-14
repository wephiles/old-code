# -*- coding: utf-8 -*-
# @CreateTime : 2023/5/23 023 20:25
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/admin.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles

from django.shortcuts import render, redirect
from django import forms
from django.core.exceptions import ValidationError

from my_site import models
from my_site.utils.pagination import Pagination
from my_site.utils.bootstrap import BootStrapModelForm
from my_site.utils.encrypt import md5


def admin_list(request, ):
    """
    管理员列表
    Parameters
    ----------
    request

    Returns
    -------

    """
    # 构造搜索
    data_dict = {}
    # 如果data_dict为空，则是找到所有的
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['username__contains'] = search_data

    query_set = models.Admin.objects.filter(**data_dict)
    # 分页
    page_object = Pagination(request, query_set)
    context = {
        'queryset': query_set,
        'pagestring': page_object.html(),
        'searchdata': search_data,
    }

    return render(request, "admin_list.html", context)


class AdminModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label='确认密码',
        # 输入密码的时候，显示**或者··，而不是直接显示密码原文
        widget=forms.PasswordInput(render_value=True))

    class Meta(object):
        model = models.Admin
        fields = ('username', 'password', 'confirm_password')
        # 输入密码的时候，显示**或者··，而不是直接显示密码原文

        widgets = {
            'password': forms.PasswordInput(render_value=True),
            # render_value=True表示，输入密码不一致后，不会清空密码
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        confirm = md5(self.cleaned_data.get('confirm_password'))
        if confirm != pwd:
            raise ValidationError('密码不一致')
        # return以后，会放到clean_data里面，form.save以后，会保存到数据库中！！！注意这一点
        # 返回的是什么字段，那么保存的就是什么字段
        return confirm


def admin_add(request, ):
    """
    添加管理员

    Parameters
    ----------
    request

    Returns
    -------

    """

    title = '添加管理员'
    if request.method == 'GET':
        form = AdminModelForm()
        context = {
            'title': title,
            'form': form,
        }
        # return render(request, "admin_add.html", context)
        return render(request, "change.html", context)

    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'change.html', {'title': title, 'form': form, })
# END
