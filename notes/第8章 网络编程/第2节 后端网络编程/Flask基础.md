# Flask基础

---



## url_for详解

`url_for`第一个参数，应该是视图函数的名字的字符串。后面的参数就是传递给`url`。如果传递的参数之前在`url`中已经定义了，那么这个参数被当成`path`的形式给`url`。如果这个参数之前没有在`url`中定义，那么将变成查询字符串的形式放到`url`中。

```python
@app.route('/')
def my_list(page):
    return 'my list'

print(url_for('my_list', page=1, count=2))
```

### 为什么使用`url_for`

1. 将来如果修改了`URL`，但没有修改该URL对应的函数名，就不用了到处替换URL
2. `url_for`会自动的处理那些特殊的字符，不需要手动处理。