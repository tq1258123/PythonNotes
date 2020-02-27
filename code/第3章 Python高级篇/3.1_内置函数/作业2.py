# -*- coding: utf-8 -*-
# @Time     : 2019/12/31 20:20
# @Author   : 童庆
# @FileName : 作业2.py
# @Software : PyCharm


'''
给字典的值加sb
'''

l = [{'name':'alex'},{'name':'y'}]
print(list(map(lambda x: x['name'] + 'sb', l)))