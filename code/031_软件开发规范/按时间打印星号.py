# -*- coding: utf-8 -*-
# @Time     : 2020/1/7 19:22
# @Author   : 童庆
# @FileName : 按时间打印星号.py
# @Software : PyCharm


import time
for i in range(0, 101, 2):
    time.sleep(0.1)
    char_num = i//2
    pen_str = '\r%s%%:%s\n' % (i, '*' * char_num) if i == 100 else '\r%s%%: %s' % (i, '*' * char_num)
    print(pen_str, end='', flush=True)