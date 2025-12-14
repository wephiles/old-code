from django.db import models


# Create your models here.

class UserInfo(models.Model):  # 必须这么写
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    # size = models.IntegerField(default=0)
    # data = models.IntegerField(null=True, blank=True)


# # 上面代码相当于下面创建数据库表的代码

# create table app名称_userinfo (
#     id bigint auto_increment, 
#     name varchar(32),
#     password varchar(64),
#     age int
# );

class Department(models.Model):
    title = models.CharField(max_length=40)


class Role(models.Model):
    caption = models.CharField(max_length=40)


# # 新建数据
# Department.objects.create(title='信息部')
# UserInfo.objects.create(name="computer", password="123456", age=18)

# --END--
