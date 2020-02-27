# -*- coding: utf-8 -*-
# @Time     : 2019/12/25 19:45
# @Author   : 童庆
# @FileName : 作业9.py
# @Software : PyCharm

'''
支持用户持续输入，Q/q退出，性别默认男，如果是女生，性别输入女
'''

def func(name, age, edu, gender='男'):
    with open('student.txt', mode='a', encoding='utf-8') as f:
        f.write(name+'_'+gender+'_'+age+'_'+edu+'\n')

while 1:
    content = input('是否输入学生信息（输入Q/q退出）:')
    if content.upper() == 'Q':
        break
    else:
        name = input('请输入名字：')
        gender = input('请输入性别:')
        age = input('请输入年龄：')
        edu = input('请输入学历：')
        if gender == '':
            func(name, age, edu)
        else:
            func(name, age, edu, gender)