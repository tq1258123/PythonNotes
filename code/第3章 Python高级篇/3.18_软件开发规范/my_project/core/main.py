# -*- coding: utf-8 -*-
# @Time     : 2020/1/7 16:49
# @Author   : 童庆
# @FileName : main.py
# @Software : PyCharm

from core import search

def home():
    print('欢迎来到员工信息查询中心')
    operate_lst = ['查询', '修改', '删除', '添加']
    for index, item in enumerate(operate_lst, 1):
        print(index, item)
    num = int(input('请选择你要做的操作:'))  # 异常处理
    if num == 1:
        search.select()