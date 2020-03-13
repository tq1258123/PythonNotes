# -*- coding: utf-8 -*-
# @Time     : 2020/3/13 10:35
# @Author   : 童庆
# @FileName : 使用Python操作MongoDB.py
# @Software : PyCharm


# 使用MongoClient建立连接
from pymongo import MongoClient
from bson.objectid import ObjectId

conn = MongoClient()
# 创建数据库，没有插入数据时不显示
db = conn.mydb
# 插入数据
rs = db.users.insert_many([{'name': 'xinping', 'province': '北京', 'age': 25},
                     {'name': 'user1', 'province': '北京', 'age': 24}])
# 单条查询
rs = db.users.find_one()
print(rs)
# 查询所有文档
for item in db.users.find():
    print(item)
# 条件查询
for item in db.users.find({"age":24}):
    print(item)
# 统计查询
count = db.users.find({"age":{"$lt":25}}).count()
print("count={0}".format(count))
# 根据_id查询文档
rs = db.users.find_one({"_id":ObjectId('5e6af2f6df0cc62638d0ef7e')})
print(rs)
# 结果排序
for item in db.users.find().sort("age"):
    print(item)
# 更新文档
db.users.update({'_id':ObjectId('5e6af2f6df0cc62638d0ef7e')}, {'$set':{'name':'张三'}})
# 删除文档
db.users.remove({'name':'张三'})
db.users.remove()