# -*- coding: utf-8 -*-
# @Time     : 2019/12/25 19:19
# @Author   : 童庆
# @FileName : 作业1.py
# @Software : PyCharm

'''
写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者
'''

# 第一种方法
list1 = ['皇阿玛', '纯妃', '贵妃', '脾肺', '咖啡']
def func1(lst):
    result = []
    for i in range(len(list1)):
        if i%2 == 1:
            result.append(list1[i])
    return result

ret = func1(list1)
print(ret)

# 第二种方法
def func2(lst):
    return lst[1::2]  # 从第一个开始，每个两个取一个

print(func2(list1))