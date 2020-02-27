# -*- coding: utf-8 -*-
# @Time     : 2020/2/27 14:06
# @Author   : 童庆
# @FileName : 2.装饰器传参数.py
# @Software : PyCharm


import time

a = 5
b = 1


def pre_str(pre=''):
    def decorator(func):
        def inner(a, b):
            print(f'输入参数 a={a},b={b}')
            f1 = func(a,b)
            print(f'当前时间是 = {time.ctime()}')
            return f1
        return inner
    return decorator


@pre_str('add')
def add(a,b):
    return a + b


@pre_str('sub')
def sub(a,b):
    return a - b


print(f'{a} + {b} = {add(a,b)}')
print(f'{a} - {b} = {sub(a,b)}')