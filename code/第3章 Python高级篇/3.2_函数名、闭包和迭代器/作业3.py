# -*- coding: utf-8 -*-
# @Time     : 2019/12/29 15:19
# @Author   : 童庆
# @FileName : 作业3.py
# @Software : PyCharm


# 枚举
lst = ['哈哈', '吼吼', '嘿嘿', '嘻嘻']
for i in enumerate(lst):
    print(i)
for i in enumerate(lst, 1):
    print(i)
for i, v in enumerate(lst, 1):
    print(i, v)