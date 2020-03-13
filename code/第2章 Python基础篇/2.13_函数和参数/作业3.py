# -*- coding: utf-8 -*-
# @Time     : 2019/12/25 19:23
# @Author   : 童庆
# @FileName : 作业3.py
# @Software : PyCharm


'''
写函数，检查传入列表的长度，如果大于2，将列表的前两项内容返回给调用者
'''

def func(a):
    if len(a) > 2:
        return a[0:2]

print(func([2,3,4]))