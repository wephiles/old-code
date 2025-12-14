# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/29 029 21:09
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/muti_inherit.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

class A(object):
    pass


class B(A):
    pass


class C(B):
    pass


class D(object):
    pass


class E(D, C):
    pass


class F(object):
    pass


class G(F):
    pass


class H(C, G):
    pass


class Foo(E, H):
    pass


obj = Foo()

print(E.__mro__)
print(H.__mro__)
print(Foo.__mro__)

"""
L(Foo + L(E) + L(H))

L(E) = (D, object) + (C, B, A, object)

E 找出 并取出第一个元组的表头(D)和后面的元组 **除了表头** (C)以外的类名做比较，
    如果D！=B、A、object中的任意一个，那么就将这第一个元组的表头拿出来
    
得到 E D

L(E) = (object) + (C, B, A, object)
再去取第一个表的表头(object),发现在后面的表(除了表头以外的其他所有表)中能找到,于是就放着.
这时候去取下一个表的表头(C),找除这个表头所在表以外的所有表,没找到,所以把C取出来.

得到 E D C

再从第一个表里面开始找(每次都是从最开始的第一个表里面去找) 是object,其他表里面有,不管他,从下一个表里面找,
B A 依次按照上述方式寻找

得到 E D C B A 
于是最后只剩下object,拿出来

得到 E D C B A object

==> 所以E的继承关系为:
E D C B A object


同理,H的继承关系为:
==> H C B A G F object

于是Foo的继承关系为:
L(E D C B A object) + L(H C B A G F object)
==> Foo E D H C B A G F object
如果第一个表头的元素 在 其他的表里(除了表头以外)能够找到,那么就先跳过第一个表的这个表头元素转去判断下一个表的表头元素是否能够
在其他的表中找到(不判断表头元素.)
"""


# --END--
