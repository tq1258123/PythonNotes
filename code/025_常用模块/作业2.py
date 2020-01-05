# -*- coding: utf-8 -*-
# @Time     : 2020/1/5 15:44
# @Author   : 童庆
# @FileName : 作业2.py
# @Software : PyCharm


# 计算时差
import time

str_time1 = '2018-08-19 22:10:8'
str_time2 = '2018-08-20 11:07:3'
struct_t1 = time.strptime(str_time1, '%Y-%m-%d %H:%M:%S')
struct_t2 = time.strptime(str_time2, '%Y-%m-%d %H:%M:%S')
timestamp1 = time.mktime(struct_t1)
timestamp2 = time.mktime(struct_t2)
sub_time = timestamp2 - timestamp1
gm_time = time.gmtime(sub_time)
print(
'过去了%d年%d月%d日%d小时%d分钟%d秒' % (
gm_time.tm_year-1970,
gm_time.tm_mon-1,
gm_time.tm_yday,
gm_time.tm_hour,
gm_time.tm_min,
gm_time.tm_sec))