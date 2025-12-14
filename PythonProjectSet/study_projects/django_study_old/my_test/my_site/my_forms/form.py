# -*- coding: utf-8 -*-
# @CreateTime : 2023/5/18 018 21:01
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/form.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles

from django import forms
from my_site import models
from django.core.validators import RegexValidator
from django.core.validators import ValidationError
from my_site.utils.bootstrap import BootStrapModelForm


# forms.ModelForm
class UserModelForm(BootStrapModelForm):
    name = forms.CharField(min_length=3, label="用户名")

    # password = forms.CharField(min_length=3, label="密码")

    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "create_time", "depart", "gender"]
        exclude = []
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     'age': forms.TextInput(attrs={'class': 'form-control'}),
        # }

    # # 继承自定义的BootStrapModelForm类后，这段代码可以省略
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     # 循环找到所有的插件 添加class样式
    #     for name, field in self.fields.items():
    #
    #         # 如果不想给password字段设置样式：使用下面两行
    #         # if name == 'password':
    #         #     continue
    #
    #         # 字段中如果有属性，那么保留，否则增加
    #         if field.widget.attrs:
    #             field.widget.attrs['class'] = 'form-control'
    #             field.widget.attrs['placeholder'] = field.label
    #         else:
    #             if name == 'create_time':
    #                 field.widget.attrs = {'class': 'form-control',
    #                                       'placeholder': field.label,
    #                                       'autocomplete': 'off',
    #                                       }
    #             else:
    #                 field.widget.attrs = {'class': 'form-control',
    #                                       'placeholder': field.label}


class PrettyNumberModelForm(BootStrapModelForm):
    # mobile = forms.CharField(label="手机号", )

    # min_length=11, max_length=11,
    # 验证方式1：
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1\d{10}$', '手机号格式错误，请重新输入！')],
    )

    class Meta:
        model = models.PrettyNumber
        fields = ("mobile", "prices", "level", "state")
        # 或者写：fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for name, field in self.fields.items():
    #         field.widget.attrs = {
    #             'class': 'form-control',
    #             'placeholder': field.label,
    #         }

    # 验证方式2：
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        exists = models.PrettyNumber.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")
        # if len(txt_mobile) != 11:
        #     raise ValidationError('格式错误')
        return txt_mobile


class PrettyNumberEditModelForm(BootStrapModelForm):
    # disabled表示不能进行编辑
    # mobile = forms.CharField(label="手机号", disabled=True)
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1\d{10}$', '手机号格式错误，请重新输入！')],
        disabled=True
    )

    class Meta:
        model = models.PrettyNumber
        fields = ("mobile", "prices", "level", "state")

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for name, field in self.fields.items():
    #         field.widget.attrs = {
    #             'class': 'form-control',
    #             'placeholder': field.label,
    #         }

    # # 判断手机号是否存在、输入的手机号是否格式错误（如果手机号允许编辑）现在不允许编辑
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        # 当前编辑那一行的ID
        edit_id = self.instance.pk
        if models.PrettyNumber.objects.exclude(id=edit_id).filter(mobile=txt_mobile).exists():
            raise ValidationError("手机号已存在")
        # if len(txt_mobile) != 11:
        #     raise ValidationError('格式错误')
        return txt_mobile

# END
