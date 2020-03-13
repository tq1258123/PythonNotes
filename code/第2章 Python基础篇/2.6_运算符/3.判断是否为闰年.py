# -*- coding: utf-8 -*-
# @Time     : 2019/11/8 16:21
# @Author   : 童庆
# @FileName : 输入年份判断是否为闰年.py
# @Software : PyCharm

# 闰年说明：四年一闰，百年不闰，400年再闰
year = int(input('请输入年份：'))

is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(is_leap)