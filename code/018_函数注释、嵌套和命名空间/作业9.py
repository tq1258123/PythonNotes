# -*- coding: utf-8 -*-
# @Time     : 2019/12/26 23:04
# @Author   : 童庆
# @FileName : 作业9.py
# @Software : PyCharm


'''
注册功能
'''
def regist():
    print('欢迎进入注册系统')
    while 1:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        if username == '' or password == '':
            print('用户名或密码不合法')
            continue
        # 校验用户名是否已经存在
        f = open('df.txt', mode='r+', encoding="utf-8")
        for line in f:
            if username == line.split('@@')[0]:
                print('对不起，该用户名已经被注册，请重新注册')
                break
        else:  # 没注册过
            f.write('\n' + username + '@@' + password)
            print('注册成功了')
            return

regist()