# -*- coding: utf-8 -*-
# @Time     : 2020/2/27 13:55
# @Author   : 童庆
# @FileName : 1.简单装饰器.py
# @Software : PyCharm

import time

a = 5
b = 1


def decorator(func):

    def inner(a, b):
        print(f'输入参数 a={a},b={b}')
        f1 = func(a,b)
        print(f'当前时间是 = {time.ctime()}')
        return f1
    return inner


@decorator
def add(a, b):
    return a + b


@decorator
def sub(a, b):
    return a - b


print(f'{a} + {b} = {add(a,b)}')
print(f'{a} - {b} = {sub(a,b)}')