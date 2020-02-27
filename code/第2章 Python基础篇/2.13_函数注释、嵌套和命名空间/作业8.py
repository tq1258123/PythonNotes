# -*- coding: utf-8 -*-
# @Time     : 2019/12/26 23:01
# @Author   : 童庆
# @FileName : 作业8.py
# @Software : PyCharm


'''
面试题：写出输出结果
'''
def calc(a,b,c,d=1,e=2):
    return (a+b)*(c-d)+e

print(calc(1,2,3,4,5))
# print(calc(1,2))
print(calc(e=4,c=5,a=2,b=3))
print(calc(1,2,3))
print(calc(1,2,3,e=4))
# print(calc(1,2,3,d=5,4))

def extendList(val, list=[]): # 默认值如果是可变的的数据类型，每次使用的是同一个
    list.append(val)
    return list

list1 = extendList(10)  # 在默认列表里添加了10
list2 = extendList(123,[])  # 使用的是默认空列表
list3 = extendList('a')

print(list1)
print(list2)
print(list3)