# -*- coding: utf-8 -*-
# @Time     : 2020/3/13 7:37
# @Author   : 童庆
# @FileName : 数据库更新操作.py
# @Software : PyCharm


import pymysql
# 打开数据库连接
db = pymysql.connect(host="192.168.0.105", user="root", password="582153",
                    database="mytestdb", port=3306)
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL插入预计
sql = "update employee set age='%d' where id = %s" % (28, 1)
try:
    # 执行sql语句
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e)
finally:
    # 关闭数据库
    db.close()