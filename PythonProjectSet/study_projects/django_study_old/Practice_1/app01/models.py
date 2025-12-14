from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(null=True, blank=True)
    # size = models.IntegerField(default=2)
    # height = models.IntegerField(null=True, blank=True)


class Department(models.Model):
    title = models.CharField(max_length=16)

# class Role(models.Model):
#     caption = models.CharField(max_length=16)


"""
执行上面语句，相当于：
create table app01_userinfo (
    id bigint auto_increment primary key,
    name varchar(32),
    password varchar(64),
    age int
)
"""


# # 新建数据 insert into app01_department （title） values（"销售部"）
# Department.objects.create(title='销售部')
#
# UserInfo.objects.create(username="buweishi", password="123456", age=19)


# END
