# random模块

---

### 功能

1. 取随机小数
2. 取随机整数：彩票，抽奖
3. 从一个列表中随机抽取值：抽奖
4. 打乱一个列表：洗牌

```python
import random

print(random.random())  # 取0-1之间的小数
print(random.uniform(1,2))  # 取1-2之间的小数
print(random.randint(1,2))  # [1-2]包含1和2
print(random.randrange(1,2))  # [1,2)有1没有2
print(random.randrange(1,200,2))
```

```python
import random

l = ['a','b',(1,2),123]
print(random.choice(l))  # 随机抽取
print(random.sample(l,2)) # 从列表中抽取两次 sample允许抽多次，不重复

# 在原列表的基础上直接修改，节省空间
random.shuffle(l)  # 打乱原列表
print(l)
```

### 作业

生成随机验证码

```python
import random

# 数字验证码
def code(n=6):
    s = ''
    for i in range(n):
        num = random.randint(0,9)
        s += str(num)
    return s

print(code(4))
print(code())

# 数字和字母验证码
def code(n=6):
    s = ''
    for i in range(n):
        # 生成随机的字母，数字各一个，再随机抽取
        num = str(random.randint(0,9))
        alpha_upper = chr(random.randint(65,90))  # 大写范围  小写从97开始
        alpha_lower = chr(random.randint(97,122))
        res = random.choice([num,alpha_upper,alpha_lower])
        s += res
    return s

print(code(4))
print(code())

# 前两个功能合并
def code(n=6, alpha=True):
    s = ''
    for i in range(n):
        # 生成随机的字母，数字各一个，再随机抽取
        res = str(random.randint(0,9))
        if alpha:
            alpha_upper = chr(random.randint(65,90))  # 大写范围  小写从97开始
            alpha_lower = chr(random.randint(97,122))
            res = random.choice([res,alpha_upper,alpha_lower])
        s += res
    return s

print(code(4))
print(code())
```

