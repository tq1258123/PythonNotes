# -*- coding: utf-8 -*-
# @Time     : 2020/1/8 16:48
# @Author   : 童庆
# @FileName : 作业1.py
# @Software : PyCharm


"""
定义一个类，其中有计算圆周长和面积的方法
"""


class Circle:
    def __init__(self, r):
        self.r = r
        self.pi = 3.14

    def long(self):
        return 2 * self.pi * self.r

    def mianji(self):
        return self.pi * self.r ** 2


obj = Circle(5)
print(obj.long())
print(obj.mianji())