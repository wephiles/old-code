#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime : 2024/12/30 19:31
# @Author     : wephiles@20866
# @IDE        : PyCharm
# @ProjectName: DesignPattern
# @FileName   : DesignPattern/抽象工厂模式.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

from abc import ABCMeta, abstractmethod


# ----- 抽象产品 -----
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass


class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass


class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass


# ----- 抽象工厂 -----

class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass


# ----- 具体产品 -----

class SmallShell(PhoneShell):
    def show_shell(self):
        print('小手机壳')


class BigShell(PhoneShell):
    def show_shell(self):
        print('大手机壳')


class AppleShell(PhoneShell):
    def show_shell(self):
        print('苹果手机壳')


class SnapDragon(CPU):
    def show_cpu(self):
        print('骁龙CPU')


class MediaTekCPU(CPU):
    def show_cpu(self):
        print('联发科CPU')


class AppleCpu(CPU):
    def show_cpu(self):
        print('IOS CPU')


class AndroidOs(OS):
    def show_os(self):
        print('安卓OS')


class IOS(OS):
    def show_os(self):
        print('IOS')


# ----- 具体工厂 -----

class MiFactory(PhoneFactory):
    def make_cpu(self):
        return SnapDragon()

    def make_shell(self):
        return BigShell()

    def make_os(self):
        return AndroidOs()


class HuaWeiFactory(PhoneFactory):
    def make_cpu(self):
        return MediaTekCPU()

    def make_shell(self):
        return SmallShell()

    def make_os(self):
        return AndroidOs()


class IphoneFactory(PhoneFactory):
    def make_cpu(self):
        return AppleCpu()

    def make_shell(self):
        return AppleShell()

    def make_os(self):
        return IOS()


# ----- 客户端 -----

class Phone:
    def __init__(self, cpu, os, shell):
        self.cpu = cpu
        self.os = os
        self.shell = shell

    def show_info(self):
        print('手机信息')
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_shell()


def make_phone(factory):
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()
    return Phone(cpu, os, shell)


p1 = make_phone(MiFactory())
p1.show_info()

# --END--
