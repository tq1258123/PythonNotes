# -*- coding: utf-8 -*-
# @Time     : 2020/3/2 23:11
# @Author   : 童庆
# @FileName : 1.字符串基本操作.py
# @Software : PyCharm


s1 = 'hello ' * 3
print(s1)
s2 = 'world'
s1 += s2
print(s1)
print('ll' in s1)
print('good' in s1)
str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2]) # c python中索引-是从0开始
# 字符串切片(从指定的开始索引到指定的结束索引)
# [x:y:z] x表示开始索引，y表示结束索引，z代表间隔长度
print(str2[2:5])
print(str2[2:])
print(str2[2::2])
print(str2[::2])
print(str2[::-1])
print(str2[-3:-1])