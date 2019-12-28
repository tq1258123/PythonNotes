# -*- coding: utf-8 -*-
# @Time     : 2019/12/26 22:58
# @Author   : 童庆
# @FileName : 作业4.py
# @Software : PyCharm


'''
判断输出结果
'''
a = 2
def func():
    global a
    a += 1
print(a)
func()