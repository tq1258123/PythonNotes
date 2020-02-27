# -*- coding: utf-8 -*-
# @Time     : 2019/12/31 20:30
# @Author   : 童庆
# @FileName : 作业7.py
# @Software : PyCharm


'''
按值从小到大排序
'''

l1 = [
    {'sales_volum':0},
    {'sales_volum':337},
    {'sales_volum':475},
    {'sales_volum':396},
    {'sales_volum':172},
    {'sales_volum':9},
    {'sales_volum':58},
    {'sales_volum':272},
    {'sales_volum':456},
    {'sales_volum':440},
    {'sales_volum':239},
    {'sales_volum':108}
]
print(sorted(l1, key=lambda x:x['sales_volum']))