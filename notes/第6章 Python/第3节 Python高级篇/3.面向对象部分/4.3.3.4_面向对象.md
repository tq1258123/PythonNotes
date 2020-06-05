# 面向对象4

---

## `isinstance/issubclass/type`

### `issubclass`

```python
class Base(object):
    pass
class Foo(Base):
    pass
class Bar(Foo):
    pass

# 检查第一个参数是否是第二个参数的子孙类
print(issubclass(Foo,Base))
```

### `type`

```python
class Foo(object):
    pass
obj = Foo()
print(obj,type(obj))
if type(obj) == Foo:
    print('obj和Foo是同类')
```

```python
class Foo(object):
    pass
class Bar(object):
    pass
def func(*args):
    foo_counter = 0
    bar_counter = 0
    for item in args:
        if type(item) == Foo:
            foo_counter += 1
        elif type(item) == Bar:
            bar_counter += 1
    return foo_counter,bar_counter

result = func(Foo(),Bar(),Foo())
print(result)
v1,v2 = func(Foo(),Bar(),Foo())
print(v1,v2)
```

###  `isinstance`

```python
class Foo(object):
    pass
obj = Foo()
# 检验第一个参数是否是第二个参数的实例，包括父类但不包括子类 
print(isinstance(obj,Foo))
```

## 方法和函数的区分

```python
def func():
    pass
print(func)

class Foo(object):
    def detail(self):
        pass 
obj = Foo()
print(obj.detail)
```

```python
class Foo(object):
    def f1(self):
        pass

obj = Foo()
print(obj.f1)  # 方法
print(Foo.f1)  # 函数，参数需要再传
```

```python
class Foo(object):
    def f1(self):
        pass
    def f2(self):
        pass
    def f3(self):
        pass
    list_display = [f1,f2]
    def __init__(self):
        pass

for item in Foo.list_display:
    print(item)
# 通过对象调用的是方法，直接调用的是函数
```

 ## 反射

```python
# 生成一个handler.py文件
def f1():
    print('f1')
def f2():
    print('f2')
def f3():
    print('f3')
def f4():
    print('f4')
```

```python
# 调用handler
import handler
from types import FunctionType

while True:
    print("""
    系统支持的函数有：
    1.f1
    2.f2
    3.f3
    4.f4
    """)
    val = input("请输入要执行的函数：")
    # 第一种方法
    if val == 'f1':
        handler.f1()
    elif val == 'f2':
        handler.f2()
    elif val == 'f3':
        handler.f3()
    elif val == 'f4':
        handler.f4()
    # 第二种方法
    if hasattr(handler, val):
        func = getattr(handler, val)  # 根据字符串为参数，去模块中寻找与之同名的成员
        if isinstance(func,FunctionType)
            func()
        else:
            print(func)
    else:
        print("handler无这个属性名")
```

```python
# 面向对象简单示例
class Foo(object):
    country = "中国"
    def func(self):
        pass

v = getattr(Foo,"func")
print(v)

obj = Foo()
v = getattr(obj,"func")
print(v)
```

### 总结

`v = getattr(obj,"func")`根据字符串为参数(第二个参数)，去对象(第一个参数)中寻找与之同名的成员

### 练习

```python
class Account(object):
    def login(self):
        print("登陆")
    def logout(self):
        print("注销")
    def register(self):
        print("注册")
    def run(self):
        func_list = ['login','logout','register']
        print("""
        请输入要执行的功能：
        1.登陆
        2.注销
        3.注册
        """)
        choice = int(input("请输入要执行的序号："))
        func_name = func_list(choice - 1)
        func = getattr(self, func_name)
        func()

obj = Account()
obj.run()
```

### 补充

`getattr`根据字符串的形式，去对象中找成员

`hasattr`根据字符串的形式，去判断对象中是否有成员

`setattr`根据字符串的形式，去判断对象动态的设置一个成员

`delattr`根据字符串的形式，去判断对象动态的删除一个成员

```python
# 设置一个xx.py文件
x1 = 123
def f1(arg):
    print(arg,888)
```

```python
# 模块的形式
import xx

v1 = getattr(xx,'x1')
v2 = getattr(xx,'f1')
v2("杨森")
v3 = hasattr(xx, 'x1')
print(v3)
setattr(xx,'x2',999)
v4 = getattr(xx,'x2')
setattr(xx,'f2',lambda x:x+1)
v5 = getattr(xx,'f2')
print(v5)
delattr(xx,'x1')
v6 = getattr(xx,'x1')
print(v6)
```

```python
# 面向对象的形式
class Foo(object):
    def __init__(self,a1):
        self.a1 = a1
        self.a3 = None
        
obj = Foo(1)
v1 = getattr(obj,'a1')
print(v1)

setattr(obj,'a2',2)
v2 = getattr(obj,'a2')
print(v2)
```

## 总结

反射`*****`

`isinstance/issubclass/type` `***`

方法和函数`*`

问题：你讲的什么后面可以加`()`?

`类()`,`对象()`,`函数()`,`方法()`以上所有都可以被调用

```python
def func():
    pass
class Foo(object):
    def __call__(self,*args,**kwargs)
    	pass
    def func(self):
        pass
    
obj = Foo()
print(callable(func))
print(callable(Foo))
print(callable(obj))
print(callable(obj.func))
```

## 作业

1. `super`的作用

```python
class Base:
    def f1(self):
        super().f1()
        
```

