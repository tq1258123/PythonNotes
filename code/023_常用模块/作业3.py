# -*- coding: utf-8 -*-
# @Time     : 2020/1/5 15:56
# @Author   : 童庆
# @FileName : 作业3.py
# @Software : PyCharm


# 计算文件夹的内存
import os

# 递归版本
def func(path):
    size_sum = 0
    name_lst = os.listdir(path)
    for name in name_lst:
        path_abs = os.path.join(path, name)
        if os.path.exists(path_abs):
            if os.path.isdir(path_abs):
                size = func(path_abs)
                size_sum += size
            else:
                size_sum += os.path.getsize(path_abs)
    return size_sum


ret = func(r'D:\repository\PythonNotes')
print(ret)  # 统计的结果不是完全相同的(windows系统)-->文件碎片

# 循环  堆栈思想
# 列表满足一个顺序，先进来的后出去
l = [r'D:\repository\PythonNotes']
size_sum = 0
while l:
    path = l.pop()  # path = '路径'  l = []
    path_list = os.listdir(path)
    for name in path_list:
        abs_path = os.path.join(path, name)
        if os.path.isdir(abs_path):
            l.append(abs_path)  # 再次添加文件夹里的文件夹
        else:
            size = os.path.getsize(abs_path)
            size_sum += size

print(size_sum)
