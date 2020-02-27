# -*- coding: utf-8 -*-
# @Time     : 2019/12/24 20:47
# @Author   : 童庆
# @FileName : 2.分段函数.py
# @Software : PyCharm

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3

# % 表示替代的变量
# .2 表示小数点后两位
# f 表示为浮点型
print('f(%.2f) = %.2f' % (x, y))