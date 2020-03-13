# -*- coding: utf-8 -*-
# @Time     : 2020/3/13 7:04
# @Author   : 童庆
# @FileName : 数据库批量插入操作.py
# @Software : PyCharm


import pymysql
# 打开数据库连接
db = pymysql.connect(host="192.168.0.105", user="root", password="582153",
                    database="mytestdb", port=3306)
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL插入预计
sql = "insert into employee(name, age, sex, income) values(%s, %s, %s, %s)"
ls = []
employee1 = ('张三', 22, 'F', 2000)
employee2 = ('李四', 23, 'M', 3000)
ls.append(employee1)
ls.append(employee2)
try:
    # 执行sql语句
    cursor.executemany(sql, ls)
    # 提交到数据库执行
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
finally:
    # 关闭数据库
    db.close()