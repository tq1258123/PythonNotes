# -*- coding: utf-8 -*-
# @Time     : 2019/12/25 19:30
# @Author   : 童庆
# @FileName : 作业5.py
# @Software : PyCharm

'''
写函数，接收两个数字参数，返回较大的数
'''


def func(a, b):
    return a if a > b else b  # 三元运算符,适合两个参数

print(func(10, 20))