# -*- coding: utf-8 -*-
# @Time     : 2019/12/30 11:40
# @Author   : 童庆
# @FileName : 作业1.py
# @Software : PyCharm


# 筛选长度大于三
lst = ['kobe','anthonmy','史可','吴彦','山本五十六','松下索尼阿玛尼']
ll = [name.upper() for name in lst if len(name) > 3]
print(ll)