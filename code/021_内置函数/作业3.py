# -*- coding: utf-8 -*-
# @Time     : 2019/12/31 20:22
# @Author   : 童庆
# @FileName : 作业3.py
# @Software : PyCharm


'''
筛选值大于20
'''

shares = {
    'IBM':36.6,
    'Lenovo':23.2,
    'odlboy':21.2,
    'ocean':10.2,
}

print(list(filter(lambda x:shares[x] > 20, shares)))