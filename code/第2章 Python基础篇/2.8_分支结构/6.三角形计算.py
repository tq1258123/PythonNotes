# -*- coding: utf-8 -*-
# @Time     : 2019/12/24 20:53
# @Author   : 童庆
# @FileName : 6.三角形计算.py
# @Software : PyCharm

# 输入三条边长，如果能构成三角形就计算周长和面积
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    # 海伦公式
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积: %f' % (area))
else:
    print('不能构成三角形')