# -*- coding: utf-8 -*-
# @Time     : 2019/12/30 12:56
# @Author   : 童庆
# @FileName : python.py
# @Software : PyCharm

# (x,y)，x是0 - 5偶数，y是0 - 5奇数
tu = [(x,y) for x in range(6) for y in range(6) if x % 2 == 0 and y % 2 ==1]
print(tu)