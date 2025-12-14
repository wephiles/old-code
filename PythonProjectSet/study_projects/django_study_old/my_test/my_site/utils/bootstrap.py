# -*- coding: utf-8 -*-
# @CreateTime : 2023/5/18 018 20:54
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/bootstrap.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles

from django import forms


class BootStrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件 添加样式
        for name, field in self.fields.items():
            # if name == 'password':
            #     continue
            if name == 'create_time':
                field.widget.attrs = {'class': 'form-control',
                                      'placeholder': field.label,
                                      'autocomplete': 'off',
                                      }
            else:
                field.widget.attrs = {'class': 'form-control',
                                      'placeholder': field.label}

# END
