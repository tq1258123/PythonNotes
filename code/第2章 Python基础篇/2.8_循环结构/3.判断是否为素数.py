# -*- coding: utf-8 -*-
# @Time     : 2019/12/24 21:19
# @Author   : 童庆
# @FileName : 3.判断是否为素数.py
# @Software : PyCharm

from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)