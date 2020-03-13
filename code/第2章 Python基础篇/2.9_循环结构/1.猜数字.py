# -*- coding: utf-8 -*-
# @Time     : 2019/12/24 21:06
# @Author   : 童庆
# @FileName : 1.猜数字.py
# @Software : PyCharm

import random

answer = random.randint(1, 100)
counter = 0
while 1:
    counter += 1
    number = int(input('请输入一个整数：'))
    if number < answer:
        print('小了')
    elif number > answer:
        print('大了')
    else:
        print('你猜对啦')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你真是太笨了')