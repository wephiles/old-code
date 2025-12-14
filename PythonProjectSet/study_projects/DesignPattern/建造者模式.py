#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2025/01/05 20:51
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: DesignPattern
# @FileName   : DesignPattern/建造者模式.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles


from abc import ABCMeta, abstractmethod


class Player:
    def __init__(self, face='', body='', arm='', leg=''):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return f'头:{self.face}, 身体:{self.body}, 胳膊:{self.arm}, 腿:{self.leg}'


class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    def build_body(self):
        pass

    def build_arm(self):
        pass

    def build_leg(self):
        pass


class GirlBuilder(PlayerBuilder):

    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = 'face 1'

    def build_body(self):
        self.player.body = 'body 1'

    def build_arm(self):
        self.player.arm = 'arm 1'

    def build_leg(self):
        self.player.leg = 'leg 1'


class MonsterBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = 'face 2'

    def build_body(self):
        self.player.body = 'body 2'

    def build_arm(self):
        self.player.arm = 'arm 2'

    def build_leg(self):
        self.player.leg = 'leg 2'


class PlayerDirector:
    """控制组装顺序"""

    def build_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player


# 客户端

builder = GirlBuilder()
director = PlayerDirector()
girl = director.build_player(builder)
print(girl)

# --END--
