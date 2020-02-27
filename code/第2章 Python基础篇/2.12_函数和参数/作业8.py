# -*- coding: utf-8 -*-
# @Time     : 2019/12/25 19:41
# @Author   : 童庆
# @FileName : 作业8.py
# @Software : PyCharm

'''
写函数，函数接收四个参数：姓名，性别，年龄，学历。将内容追加到student文件
'''

def func(name, gender, age, edu):
    with open('student.txt', mode='a', encoding='utf-8') as f:
        f.write(name+'_'+gender+'_'+age+'_'+edu+'\n')

name = input('请输入名字：')
gender = input('请输入性别:')
age = input('请输入年龄：')
edu = input('请输入学历：')
print(func(name, gender, age, edu))