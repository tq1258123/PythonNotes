# -*- coding: utf-8 -*-
# @Time     : 2019/12/26 23:00
# @Author   : 童庆
# @FileName : 作业7.py
# @Software : PyCharm


'''
扑克牌，返回[('红心'，'2')·····(''黑桃','2')·······]  笛卡尔积
'''
def func():
    result = []
    huase = ['红心', '黑桃', '草花', '方片']
    dianshu = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

    for hua in huase:
        for dian in dianshu:
            result.append((hua, dian))
    return result

print(func())