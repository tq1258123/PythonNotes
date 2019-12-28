# -*- coding: utf-8 -*-
# @Time     : 2019/12/26 22:59
# @Author   : 童庆
# @FileName : 作业5.py
# @Software : PyCharm


'''
写函数，传入n个数，返回字典{'max':'最大值', 'min':'最小值'}
'''
def func(*args):
	return {'max':max(args), 'min':min(args)}

print(func(1,2,3,4))