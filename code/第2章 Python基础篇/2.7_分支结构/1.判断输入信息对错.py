# -*- coding: utf-8 -*-
# @Time     : 2019/12/24 20:38
# @Author   : 童庆
# @FileName : 1.判断输入信息对错.py
# @Software : PyCharm

username = input('请输入用户名: ')
password = input('请输入口令: ')
# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
if username == 'tq1258' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')