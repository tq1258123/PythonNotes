# -*- coding: utf-8 -*-
# @Time     : 2019/12/24 21:12
# @Author   : 童庆
# @FileName : 2.乘法口诀表.py
# @Software : PyCharm

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d * %d = %d' % (i, j, i*j), end=' ')
    print()