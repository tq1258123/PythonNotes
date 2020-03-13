# -*- coding: utf-8 -*-
# @Time     : 2019/12/25 19:31
# @Author   : 童庆
# @FileName : 作业6.py
# @Software : PyCharm

'''
写函数，检查传入字典的每一个value的长度，如果大于2，保留前两个长度的内容，并将新内容返回
'''

dic = {'k1':'v1v1', 'k2':'1165', 'k3':'22'}
def func(dic):
    newdic = {}
    for k, v in dic.items():
        if len(v) > 2:
            s = v[0:2]
            newdic[k] = s
        else:
            newdic[k] = v
    return newdic

print(func(dic))