# -*- coding: utf-8 -*-
# @Time     : 2019/12/30 13:03
# @Author   : 童庆
# @FileName : 作业4.py
# @Software : PyCharm


# 元素加索引
lst =['alex', 'wusir', '老男孩', '太白']
print([el+str(index) for index, el in enumerate(lst)])