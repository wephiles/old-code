from django.db import models


# Create your models here.


class Department(models.Model):
    """
    部门管理相关数据库。
    """
    title = models.CharField(max_length=32, verbose_name="标题")  # verbose_name 注解

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """
    员工管理相关数据库。
    """
    name = models.CharField(verbose_name="员工姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    # create_time = models.DateTimeField(verbose_name="入职时间")
    create_time = models.DateField(verbose_name="入职时间")
    # to：与哪张表关联 to_field: 与表中哪一个列关联
    # Django中自动做的 在底层生成数据库的列的时候 会自动生成数据列 depart_id
    depart = models.ForeignKey(to="Department", to_field="id", verbose_name="部门", on_delete=models.CASCADE)
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)


class PrettyNumber(models.Model):
    """
    靓号管理
    """

    def __str__(self):
        return ''

    state_choices = (
        (1, "已使用"),
        (2, "未使用"),
    )
    level_choices = (
        (1, "青铜"),
        (2, "白银"),
        (3, "黄金"),
        (4, "钻石"),
        (5, "星光"),
    )
    # CharField 必须设置长度
    # 允许为空： blank=True, null=True
    mobile = models.CharField(verbose_name="号码", max_length=20)
    prices = models.IntegerField(verbose_name="价格", default=0)
    level = models.SmallIntegerField(verbose_name="等级", choices=level_choices, default=1)
    state = models.SmallIntegerField(verbose_name="状态", choices=state_choices, default=2)


class Admin(models.Model):
    """
    管理员
    """
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='用户密码', max_length=64)


# END
