# -*- coding: utf-8 -*-
# @Time     : 2020/1/7 17:45
# @Author   : 童庆
# @FileName : search.py
# @Software : PyCharm

'''
查询的逻辑
'''

from conf import settings
def select():
    condition = input('>>>')
    print(condition)
    # 收到命令要处理一下
    # 要到文件中查
    # 要打开文件
    # 文件名怎么取
    staff_info = settings.staffinfo
    with open(staff_info) as f:
        for line in f:
            print(line.strip())