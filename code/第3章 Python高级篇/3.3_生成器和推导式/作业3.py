# -*- coding: utf-8 -*-
# @Time     : 2019/12/30 12:58
# @Author   : 童庆
# @FileName : 作业3.py
# @Software : PyCharm


# [[1,2,3],[4,5,6],[7,8,9]] <--> [3,6,9]
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst = [i[2] for i in M]
print(lst)

lst = [3, 6, 9]
lst1 = [[i-2, i-1, i] for i in lst]
print(lst1)