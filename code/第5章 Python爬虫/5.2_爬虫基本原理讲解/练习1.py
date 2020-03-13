# -*- coding: utf-8 -*-
# @Time     : 2020/3/13 16:19
# @Author   : 童庆
# @FileName : 练习1.py
# @Software : PyCharm


import requests
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
response = requests.get('http://www.baidu.com', headers=headers)
print(response.status_code)