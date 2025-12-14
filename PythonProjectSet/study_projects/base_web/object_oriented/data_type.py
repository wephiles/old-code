# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/17 017 22:56
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/data_type.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

class Police:
    """警察类."""

    def __init__(self, name, age, hit_points):
        self.name = name
        self.age = age
        self.hit_points = hit_points

    def catch(self):
        """抓小偷"""
        self.hit_points += 100

    def smoking(self):
        """抽烟"""
        self.hit_points -= 50

    def shoot(self, user):
        """开枪"""
        user.hit_points -= 100
        self.hit_points -= 10


# (name="computer", age=19, hit_points=1100)
p1 = Police("computer", 19, 1100)
p2 = Police("science", 23, 1200)
p3 = Police("technology", 24, 1300)

p1.shoot(p3)
print(p1.hit_points)
print(p3.hit_points)

p3.shoot(p1)
print(p1.hit_points)
print(p3.hit_points)

# --END--
