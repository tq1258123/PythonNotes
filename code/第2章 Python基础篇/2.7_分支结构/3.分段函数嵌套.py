# -*- coding: utf-8 -*-
# @Time     : 2019/12/24 20:51
# @Author   : 童庆
# @FileName : 3.分段函数嵌套.py
# @Software : PyCharm

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))