# -*- coding: utf-8 -*-
# @Time     : 2020/1/5 16:41
# @Author   : 童庆
# @FileName : 作业1.py
# @Software : PyCharm
# 计算器


import re


# 写函数计算小字符串的结果
def atom_cal(exp):
    if '*' in exp:
        a, b = exp.split('*')
        return str(float(a) * float(b))
    elif '/' in exp:
        a, b = exp.split('/')
        return str(float(a) / float(b))


def format_exp(exp):
    exp = exp.replace('--', '+')
    exp = exp.replace('++', '+')
    exp = exp.replace('-+', '-')
    exp = exp.replace('+-', '-')
    return exp


def mul_div(exp):
    while 1:
    ret = re.search(r'\d+(\.\d+)?[*/]-?\d+(\.\d+)?', exp)
    if ret:
        atom_exp = ret.group()
        res = atom_cal(atom_exp)
        exp = exp.replace(atom_exp, res)
    else:
        return exp


def add_sub(exp):
    ret = re.findall(r'[-+]?\d+(?:\.\d+)+', exp)
    exp_sum = 0
    for i in ret:
        exp_sum += float(i)
    return exp_sum


# 乘除法先匹配
def cal(exp):
    exp = mul_div(exp)
    exp = format_exp(exp)
    exp_sum = add_sub(exp)
    return exp_sum


def main(exp):
    exp.replace(' ', '')
    while 1:
        ret = re.search(r'\([^()]+\)', exp)
        if ret:
            inner_bracket = ret.group()
            res = str(cal(inner_bracket))
            exp = exp.replace(inner_bracket, res)
            exp = format_exp(exp)
        else:
            break
    return cal(exp)


s = '1 - 2 *((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
ret = main(s)
print(ret)
print(eval(s))