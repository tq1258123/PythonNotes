# -*- coding: utf-8 -*-
# @Time     : 2020/1/5 13:40
# @Author   : 童庆
# @FileName : 1.深拷贝.py
# @Software : PyCharm

import copy

lst1 = ['金毛狮王','紫衫龙王','青翼蝠王','白眉鹰王',['张无忌','赵敏','周芷若']]
lst2 = copy.deepcopy(lst1)
lst1[4].append('小昭')
print(lst1)
print(lst2)
print(id(lst1))
print(id(lst2))