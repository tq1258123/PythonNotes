## `time`模块

---

### 功能

1. 主要用来和时间打交道
2. 时间格式
   1. 浮点型数据类型：以秒为单位`1534732642.617272`
   2. 结构化时间：元组，只能取值不能修改
   3. 格式化数据类型`2020-01-02` `%Y %m %d %H %M %S`

3. 计算机时间`1970-01-01 00:00:00 `
4. 三种时间的转换

![三种时间格式转换](D:\repository\PythonNotes\images\三种时间格式转换.png)

```python
import time

time.sleep(2)
print(123)
print(time.time())
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%c'))  # 英国人格式
print(time.localtime())  # 结构化时间

struct_time = time.localtime()
print(struct_time.tm_mon)
```

```python
import time

# 时间戳-->结构化
print(time.time())
print(time.localtime(1500000000))  # 北京时间
print(time.gmtime(1500000000))  # 伦敦时间

# 结构化-->字符串
struct_time = time.localtime(1500000000)
ret = time.strftime('%Y-%m-%d %H:%M:%S', struct_time)
print(ret)

# 字符串-->结构化
struct_time = time.strptime('2018-8-8','%Y-%m-%d')
print(struct_time)

# 结构化-->时间戳
res = time.mktime(struct_time)
print(res)
```

### 练习

1. 查看`200000000`时间戳对应的年月日

```python
import time

struct_time = time.localtime(2000000000)
ret = time.strftime('%Y:%m:%d', struct_time)
print(ret)
```

2. 请将当前时间的当前月1号的时间戳时间取出来

```python
import time

def get_time():
    st = time.localtime()
    st1= time.strptime('%s-%s-%s' % (st.tm_year, st.tm_mon, st.tm_mday), '%Y-%m-%d')
    return time.mktime(st1)

print(get_time())
```

3. 计算时差

```python
import time

str_time1 = '2018-08-19 22:10:8'
str_time2 = '2018-08-20 11:07:3'
struct_t1 = time.strptime(str_time1, '%Y-%m-%d %H:%M:%S')
struct_t2 = time.strptime(str_time2, '%Y-%m-%d %H:%M:%S')
timestamp1 = time.mktime(struct_t1)
timestamp2 = time.mktime(struct_t2)
sub_time = timestamp2 - timestamp1
gm_time = time.gmtime(sub_time)
print(
'过去了%d年%d月%d日%d小时%d分钟%d秒' % (
gm_time.tm_year-1970,
gm_time.tm_mon-1,
gm_time.tm_yday,
gm_time.tm_hour,
gm_time.tm_min,
gm_time.tm_sec))
```
