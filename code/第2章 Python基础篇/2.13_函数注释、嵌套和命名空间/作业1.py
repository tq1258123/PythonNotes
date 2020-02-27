# -*- coding: utf-8 -*-
# @Time     : 2019/12/26 22:28
# @Author   : 童庆
# @FileName : 作业1.py
# @Software : PyCharm


'''
写函数，接收n个数字，求只写参数数字的和
'''

def func1(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(func1(1,3,5))

# sum中可以直接接收一个可迭代对象，进行迭代相加
def func2(*args):
    return sum(args)

print(func2(1,2,3))