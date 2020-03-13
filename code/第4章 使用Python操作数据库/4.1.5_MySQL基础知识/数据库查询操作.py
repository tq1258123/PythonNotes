# -*- coding: utf-8 -*-
# @Time     : 2020/3/13 7:18
# @Author   : 童庆
# @FileName : 数据库查询操作.py
# @Software : PyCharm


import pymysql
# 打开数据库连接
db = pymysql.connect(host="192.168.0.105", user="root", password="582153",
                    database="mytestdb", port=3306)
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL插入预计
sql = "select * from employee where income > %d" % (2000)
try:
    # 执行sql语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        name = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("id=%s, name=%s, age=%d, sex=%s, income=%d" % (id, name, age, sex, income))
except Exception as e:
    print(e)
finally:
    # 关闭数据库
    db.close()