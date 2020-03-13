# -*- coding: utf-8 -*-
# @Time     : 2020/3/4 19:37
# @Author   : 童庆
# @FileName : 练习.py
# @Software : PyCharm


import pymysql

user = input('username:')
pwd = input('password:')

conn = pymysql.connect(host='localhost', user='root', password='582153', database='tb1')
cursor = conn.cursor()
# 连接数据库成功
sql = "select * from userinfo where username='%s' and password='%s'" % (user,pwd)
print(sql)
cursor.execute(sql)
result = cursor.fetchone()  # 只拿第一个
cursor.close()
conn.close()
print(result)