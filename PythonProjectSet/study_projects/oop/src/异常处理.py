#!/user/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2024/12/18 21:08
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: oop
# @FileName   : oop/异常处理.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

import os


class ExistsError(Exception):
    pass


class KeyInvalidException(Exception):
    pass


def func(path, prev):
    """
    去path指向的文件中去寻找前缀为prev的一行数据，获取数据并返回给调用者
    Args:
        path ():
        prev ():

    Returns:

    """
    # 假设code为 1000 表示成功 1001 表示文件不存在 1002 表示关键字为空
    response = {
        'code': 1000, 'data': None
    }
    try:
        if not os.path.exists(path):
            raise ExistsError('文件不存在')

        if not prev:
            raise KeyInvalidException('关键字为空')
        pass

    except ExistsError as _:
        response['code'] = 1001
        response['data'] = '文件不存在'

    except KeyInvalidException as _:
        response['code'] = 1002
        response['data'] = '关键字为空'

    except Exception as e:
        response['code'] = 1003
        response['data'] = '未知错误'
    return response

# --END--
