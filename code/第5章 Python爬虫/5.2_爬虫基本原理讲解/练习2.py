# -*- coding: utf-8 -*-
# @Time     : 2020/3/13 16:54
# @Author   : 童庆
# @FileName : 练习2.py
# @Software : PyCharm


import requests

try:
    response = requests.get('http://httpbin.org/get', timeout=0.1)
    print(response.status_code)
except Exception as e:
    print(e)