# -*- coding: utf-8 -*-
# @Time     : 2019/12/25 14:12
# @Author   : 童庆
# @FileName : 文件的基本操作.py
# @Software : PyCharm


# # 文件的打开和关闭
# f = open('a.txt', mode='r', encoding='utf-8')
# f.close()


# # 避免忘记关闭文件，使用with打开
# with open('a.txt', mode='r', encoding='utf-8') as f:
#     pass


# # 读取文件
# with open('a.txt', mode='r') as f:
#     a = f.read()
#     print(a)


# # 写入文件内容，会覆盖原来的内容
# with open('a.txt', mode='w+',encoding='utf-8') as f:
#     f.write('你好啊，我喜欢你')


# # 追加文件内容
# with open('a.txt', mode='a',encoding='utf-8') as f:
#     f.write('你好啊，我喜欢你')


