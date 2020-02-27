# -*- coding: utf-8 -*-
# @Time     : 2019/12/29 15:17
# @Author   : 童庆
# @FileName : 作业2.py
# @Software : PyCharm


# 等腰三角形
# 空格和星号分开打印
n = 6
for i in range(1, n):
    for k in range(2 * n - 2 * i):
        print('', end=' ')
    for j in range(2 * i - 1):
        print('*', end=' ')
    print()