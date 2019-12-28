# -*- coding: utf-8 -*-
# @Time     : 2019/12/25 19:40
# @Author   : 童庆
# @FileName : 作业7.py
# @Software : PyCharm

'''
写函数，此函数只接收一个参数且是列表，返回字典，字典的键值对为列表索引和对应元素
'''

lst = [11, 22, 33]
def func(lst):
    dic = {}
    if type(lst) == list:
        for i in range(len(lst)):
            dic[i+1] = lst[i]
        return dic
    else:
        return '不是列表'

print(func(lst))