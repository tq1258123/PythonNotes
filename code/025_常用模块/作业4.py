# -*- coding: utf-8 -*-
# @Time     : 2020/1/5 16:25
# @Author   : 童庆
# @FileName : 作业4.py
# @Software : PyCharm


# 接受一个参数，如果是文件，就执行；文件夹里`.py`执行里面的内容
import os

def func(path):
    # 判断路径是文件还是文件夹
    # 如果是文件还要是以py结尾
    # 执行py文件
    # 如果不是，重复操作
    if os.path.isfile(path) and path.endswith('.py'):
        os.system('python %s' % path)  # 模拟了在cmd中执行代码的过程
    elif os.path.isdir(path):
        for name in os.listdir(path):
            abs_path = os.path.join('path', name)
            if abs_path.endswith('.py'):
                os.system('python %s' % abs_path)

func(r'D:\repository\PythonNotes\code\006_第一个小程序')