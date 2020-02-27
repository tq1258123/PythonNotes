# -*- coding: utf-8 -*-
# @Time     : 2019/12/25 19:25
# @Author   : 童庆
# @FileName : 作业4.py
# @Software : PyCharm

'''
写函数，计算传入函数的字符串中，数字、字母、空格以及其他内容的个数，并返回结果
'''


def func(a):
    num = 0
    alpha = 0
    space = 0
    other = 0
    for i in a:
        if i.isdigit():
            num += 1
        elif i.isalpha():  # 不能判断中文
            alpha += 1
        elif i == ' ':
            space += 1
        else:
            other += 1
    return num, alpha, space, other

print(func('12sdfsd'))