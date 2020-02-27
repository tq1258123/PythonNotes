## 序列化模块

1. 序列：列表，元组，字符串，bytes
2. 序列化：把其他的数据类型转换成字符串/bytes
3. 原因：能够在网络上传输的只能是bytes，能够存储在文件里的只有bytes/字符串

```python
import json

dic = {'key':'value','key2':'value2'}
ret = json.dumps(dic)  # 序列化
print(dic)
print(ret)
res = json.loads(ret)  # 反序列化
print(res)

# 问题1:数字在转化过程中编程字符串
dic = {1:'value',2:'value'}
ret = json.dumps(dic)  # 序列化
print(dic)
print(ret)
res = json.loads(ret)  # 反序列化
print(res)

# 问题2：
dic = {1:[1,2,3],2:(4,5,'aa')}
ret = json.dumps(dic)  # 序列化
print(dic)
print(ret)
res = json.loads(ret)  # 反序列化
print(res)

# 问题3:不能序列化
dic = {1,2,'aaa'}
ret = json.dumps(dic)  # 序列化
print(dic)
print(ret)
res = json.loads(ret)  # 反序列化
print(res)

# 问题4
json.dumps({(1,2,3):123})

# 问题5
# 可以多次dump，但是不能多次load，load文件中中能有一个字典
```

- `json`

  1. 能够处理的数据类型是非常有限的：字符串，列表，字典，数字

  2. 字典中的key只能是字符串

  3. 在所有的语言之间都通用

  4. `dumps/loads dump/load`

  5. `json`是所有语言通用的一种序列化格式，只支持列表，字典，字符串，数字，字典的`key`必须是字符串

     1. `dumps/loads`：在内存里处理

        1. 在内存中做数据转换

           `dumps`数据类型转成字符串-->序列化

           `loads`字符串转成数据类型-->反序列化

```python
# 写入和读取字典
import json

dic = {'key':'value','key2':'value2'}
ret = json.dumps(dic)
with open('json_file','a') as f:
    f.write(ret)
with open('json_file','r') as f:
    str_dic = f.read()
dic = json.loads(str_dic)
print(dic)
```

2. `dump/load`：直接处理文件内容

   1. 直接将数据类型写入文件，直接从文件独处数据类型

      `dump`数据类型写入文件-->序列化

      `load`文件独处数据类型 --> 反序列化

```python
# 写入和读取字典
import json

dic = {'key':'value','key2':'value2'}
with open('json_file','a') as f:
    json.dump(dic,f)
with open('json_file','r') as f:
    dic = json.load(f)
print(dic)
```

```python
import json

dic = {'key':'value','key2':'value2'}
with open('json_file','a') as f:
    str_dic = json.dumps(dic,f)
    f.write(str_dic+'\n')
    str_dic = json.dumps(dic,f)
    f.write(str_dic+'\n')
    str_dic = json.dumps(dic,f)
    f.write(str_dic+'\n')
    
with open('json_file','r') as f:
    for line in f:
        dic = json.loads(line.strip())
        print(dic)
```

```python
# 编码问题
import json

dic = {'key':'你好'}
print(json.dumps(dic,ensure_ascii=False))
```

- `pickle`

  1. `dumps`序列化的结果只能是字节
  2. 支持在`python`中几乎所有的数据类型
  3. 只能在`python`中使用
  4. 在和文件操作的时候，需要用`rb wb`形式操作文件
  5. 可以多次`dump load`

```python
import pickle

dic = {(1,2,3):{'a','b'},1:'abc'}
ret = pickle.dumps(dic)
print(ret)
print(pickle.lads(ret))

with open('pickle_file','wb') as f:
	pickle.dump(dic,f)
with open('pickle_file','rb') as f:
	ret = pickle.load(f)
    print(ret,type(ret))

dic1 = {(1,2,3):{'a','b'},1:'abc'}
dic2 = {(1,2,3):{'a','b'},2:'abc'}
di3 = {(1,2,3):{'a','b'},3:'abc'}
dic4 = {(1,2,3):{'a','b'},4:'abc'}
with open('pickle_file','wb') as f:
	pickle.dump(dic1,f)
    pickle.dump(dic2,f)
    pickle.dump(dic3,f)
    pickle.dump(dic4,f)
with open('pickle_file','rb') as f:
    while 1:
        try:
            ret = pickle.load(f)
            print(ret,type(ret))
            ret = pickle.load(f)
            print(ret,type(ret))
            ret = pickle.load(f)
            print(ret,type(ret))
            ret = pickle.load(f)
            print(ret,type(ret))
        except EOFError:
            break
```

## 作业

1. 接受一个参数，如果是文件，就执行；文件夹里`.py`执行里面的内容

```python
import os

def func(path):
    # 判断路径是文件还是文件夹
    # 如果是文件还要是以py结尾
    # 执行py文件
    # 如果不是，重复操作
    if os.path.isfile(path) and path.endswith('.py'):
        os.system('python %s' % path)  # 模拟了在cmd中执行代码的过程
    elif os.path.isdir(path):
        for name in os.listdir(path):
            abs_path = os.path.join('path',name)
            if abs_path.endswith('.py'):
                os.system('python %s' % abs_path)
```

2. 写一个`copy`函数，接受两个参数，第一个参数是源文件的位置，第二个参数是目标位置，将源文件`copy`到新文件

```python
import os

# 需要判断这个文件之前是否存在
def copy(path1,path2):
    filename = os.path.basename(path1)
    if os.path.isdir(path2) and os.path.isdir(path2):
        path2 = os.path.join(path2,filename)
        if os.path.exists(path2):
            print('已有同名文件')
        else:
            with open(path1,'rb') as f1, open(os.path.join(path2,filename),'wb') as f2:
                content = f1.read()
                f2.write(content)
```

3. 获取某个文件所在的上一级目录

```python
import os

path = os.path.dirname()
print(path)
base_name = os.path.dirname()
print(base_name)
```

4. 发红包

```python
import random

def red_packet(money,num):
    money *= 100
    ret = random.sample(range(1,money), num-1)
    ret.sort()
    ret.insert(0,0)
    ret.append(money)
    for i in range(len(ret)):
        yield (ret[i+1]-ret[i])/100
        
ret_g = red_packet(200,10)
for money in ret_g:
    print(money)
```



