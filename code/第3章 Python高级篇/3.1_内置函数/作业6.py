# -*- coding: utf-8 -*-
# @Time     : 2019/12/31 20:28
# @Author   : 童庆
# @FileName : 作业6.py
# @Software : PyCharm


'''
筛选第一项大于二，第三项大于三
'''

l1 = [1,2,3,4,5,6]
l2 = ['oldboy','alex','wusir','太白','日天']
tu = ('**','***','****','*****')
print(list(filter(lambda x:x[0] > 2 and len(x[2]) > 3, zip(l1,l2,tu))))