# -*- coding: utf-8 -*-
# @Time     : 2019/12/26 22:57
# @Author   : 童庆
# @FileName : 作业3.py
# @Software : PyCharm


'''
写函数，传入喊中多个实参，将每个元素依次添加到args里(函数参数打散)
'''
def func(*args):
    print(args)

func(*[1, 2, 3], *'你好啊')