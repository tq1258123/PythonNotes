# -*- coding: utf-8 -*-
# @Time     : 2019/12/31 19:54
# @Author   : 童庆
# @FileName : 作业1.py
# @Software : PyCharm


'''
给列表每个元素加_sb
'''

name = ['oldboy', 'alex', 'wusir']
print(list(map(lambda x: x + '_sb', name)))