# -*- coding: utf-8 -*-
# @Time     : 2019/12/24 20:53
# @Author   : 童庆
# @FileName : 5.百分制成绩转换为等级制成绩.py
# @Software : PyCharm

score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是:', grade)