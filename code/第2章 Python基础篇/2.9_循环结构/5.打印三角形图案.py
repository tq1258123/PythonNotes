# -*- coding: utf-8 -*-
# @Time     : 2019/12/24 21:22
# @Author   : 童庆
# @FileName : 打印三角形图案.py
# @Software : PyCharm

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()