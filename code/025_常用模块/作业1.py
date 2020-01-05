# -*- coding: utf-8 -*-
# @Time     : 2020/1/5 15:33
# @Author   : 童庆
# @FileName : 作业1.py
# @Software : PyCharm


import random

# 数字验证码
def code(n=6):
    s = ''
    for i in range(n):
        num = random.randint(0,9)
        s += str(num)
    return s

print(code(4))
print(code())

# 数字和字母验证码
def code(n=6):
    s = ''
    for i in range(n):
        # 生成随机的字母，数字各一个，再随机抽取
        num = str(random.randint(0,9))
        alpha_upper = chr(random.randint(65,90))  # 大写范围  小写从97开始
        alpha_lower = chr(random.randint(97,122))
        res = random.choice([num,alpha_upper,alpha_lower])
        s += res
    return s

print(code(4))
print(code())

# 前两个功能合并
def code(n=6, alpha=True):
    s = ''
    for i in range(n):
        # 生成随机的字母，数字各一个，再随机抽取
        res = str(random.randint(0,9))
        if alpha:
            alpha_upper = chr(random.randint(65,90))  # 大写范围  小写从97开始
            alpha_lower = chr(random.randint(97,122))
            res = random.choice([res,alpha_upper,alpha_lower])
        s += res
    return s

print(code(4))
print(code())