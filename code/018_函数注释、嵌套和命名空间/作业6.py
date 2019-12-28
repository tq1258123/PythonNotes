# -*- coding: utf-8 -*-
# @Time     : 2019/12/26 22:59
# @Author   : 童庆
# @FileName : 作业6.py
# @Software : PyCharm


'''
计算阶乘
'''
def func(n):
    sum = 1
    while n >= 1:
        sum = sum * n
        n = n -1
    return sum

print(func(5))