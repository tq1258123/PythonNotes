# -*- coding: utf-8 -*-
# @Time     : 2020/3/2 22:52
# @Author   : 童庆
# @FileName : Python编码.py
# @Software : PyCharm


# 英文无论在什么格式下都能正常显示
print('abc')
print('abc'.encode('utf8'))
print('abc'.encode('ascii'))
print('哈哈')
print('哈哈'.encode('utf8'))
# ascii码中没有中文，会报错
# print('哈哈'.encode('ascii'))