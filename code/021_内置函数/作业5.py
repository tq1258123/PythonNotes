# -*- coding: utf-8 -*-
# @Time     : 2019/12/31 20:26
# @Author   : 童庆
# @FileName : 作业5.py
# @Software : PyCharm


'''
计算股价大于100
'''

portfolio = [
    {'name':'IBM','shares':100,'price':91.1},
    {'name':'APPL','shares':50,'price':543.22},
    {'name':'FB','shares':200,'price':21.09},
    {'name':'HPQ','shares':35,'price':31.75},
    {'name':'YHOO','shares':45,'price':16.35},
    {'name':'ACNE','shares':75,'price':115.65}
]
print(list(filter(lambda x:x['price'] > 100, portfolio)))