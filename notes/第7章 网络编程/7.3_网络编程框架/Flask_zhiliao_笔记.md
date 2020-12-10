# Flask_zhiliao_笔记

---

## url详解：

URL是Uniform Resourse Locator的简写，统一资源定位符。

一个URL由一下几部分组成：

`scheme://host:port/path/?query-string=xxx#anchor`

## web服务器和应用服务器以及web用于框架

### web服务器

负责处理http请求，响应静态文件，常见的有Apache, Nginx以及微软的IIS.

### 应用服务器

负责处理逻辑的服务器，比如php，Python的代码，是不能直接通过nginx这种web服务器来处理的，只能通过应用服务器来处理，常见的应用服务器有uwsgi, tomcat等。

### web应用框架

一般使用某种语言，封装了常用的web功能的框架就是web应用框架，flask，Django，以及Java中的SSH框架都是web应用框架。

## debug模式

### 为什么要开启DEBUG模式

1. 如果开启了DEBUG模式，那么在代码中如果抛出了异常，在浏览器的页面中可以看到具体的错误信息，以及具体的错误代码位置。方便开发者调试。
2. 如果开启了DEBUG模式，那么以后在Python代码中修改了任何代码，只要按ctrl + s，flask就会自动的重新加载整个网站。不需要手动点击重新运行。

### 配置DEBUG模式的四种方式

1. 在`app.run()`中传递一个参数`debug=True`就可以开启`DEBUG`
2. `app.debug = True`
3. `app.config.updata(DEBUG=True)`DEBUG要大写
4. 通过配置文件的兴衰设置DEBUG模式：`app.config.from_object(config)`

### PIN码

如果想要在网页上调试代码，那么应该输入`PIN`码。

## config

### 使用`app.config.from_object`的方式加载配置文件

1. 导入`import config`
2. 使用`app.config.from_object(config)`

### 使用`app.config.from_pyfile`的方式加载配置文件

`app.config.from_pyfile('config.py')`，这个地方必须要写文件的全名，后缀名不能少。

1. 这种方式，加载配置文件，不局限于只能使用`py`文件，普通的`txt`文件同样也适合。
2. 这种方式，可以传递`silent=True`，那么这个静态文件没有找到时不会报错。

## URL与视图函数的映射

### 传递参数

传递参数的语法是：`/<参数名>/`，然后在视图函数中，也要定义同名的参数。

### 参数的数据类型

1. 如果没有指定具体的数据类型，默认就是`string`类型

2. `int`数据类型只能传递`int`类型

3. `float`传递浮点型

4. `path`数据类型可以接收路径，包含`/`

5. `uuid`数据类型只能接收符合`uuid`的字符串。是一个全宇宙都唯一的字符串，一般可以用来作为表的主键。

6. `any`数据类型可以在一个`url`中指定多个路径

   ```python
   @app.route('/<any(blog,user):url_path>/<id>/')
   def detail(url_path,id):
       if url_path == 'blog':
           return '博客详情：%s' % id
       else:
           return '用户详情：%s' % id
   ```

### 接收用户传递的参数

1. 使用path的形式(将参数嵌入到路径中)

2. 使用查询字符串的方式，`?key=value`

   ```python
   @app.route('/d/')
   def d():
       wd = request.args.get('wd')
       ie = request.args.get('ie')
       return '您通过查询字符串的方式传递的参数是：%s %s' % (wd, ie)
   ```

3. 如果你的页面想要做`SEO优化`，推荐使用第一种，如果不在乎搜索引擎优化则可以使用第二种

## url_for

### `url_for`的基本使用

`url_for`第一个参数，应该是驶入函数的名字的字符串，后面的参数就是传递给`url`，如果传递的参数之前在`url`中已经定义了，那么这个参数就会被当成`path`的形式给`url`。如果这个参数之前没有在`url`中定义，那么将变成查询字符串的形式放到`url`中。

```python
@app.route('/list/<page>/')
def my_list(page):
    return 'my list'

print(url_for('my_list', page=1, count=2))
# /my_list/1/?count=2
```

### 为什么需要url_for

1. 将来如果修改URL，但没有修改URL对应的函数名，就不用了导出修改了。
2. `url_for`会自动的处理那些特殊的字符串，不需要手动处理。

```python
url = url_for('login', next='/')
# /login/?next=%2F
# 自动编码
```

3. 强烈建议以后在使用url的时候，使用`url_for`来反转`url`。

## 自定义URL转换器

### 自定义URL转换器的方式

1. 实现一个类，继承自`BaseConverter`

2. 在自定义的类中，重写`regex`，也就是这个变量的正则表达式

3. 将自定义的类，映射到`app.url_map.converters`上

   ```python
   class TelephoneConverter(BaseConverter):
       regex = r'1[34578]\d{9}'
   app.url_map.converters['tel'] = TelephoneConverter
   ```

###  `to_python`的作用

会将url中 的参数经过解释后传递给视图函数

### `to_url`的作用

在这个方法的返回值，将会在调用url_for函数的时候生成符合要求的URL形式。

## 必会的小细节知识点

### 在局域网中让其他电脑访问我的网站

如果想在同一个局域网下的其他电脑访问自己电脑上的Flask网站，那么可以设置`host="0.0.0.0"`后就能访问

### 指定端口号

Flask项目，默认使用`5000`端口，可以自己重新设置

### url唯一

在定义url的时候，一定要记得在最后加一个斜杠

1. 如果不加斜杠，那么在浏览器中访问这个url时加了斜杠，那么就会访问不到。
2. 搜索引擎会将不加斜杠的和加斜杠的视为两个不同的url，其实加和不加斜杠的都是同一个url，那么就会给搜索引擎造成一个误解。

### `GET`请求和`POST`请求

在网络请求中有许多请求方式，如`GET POST DELET PUT`等。

1. `GET`请求：只会在服务器上获取资源，不会更改服务器的状态。
2. `POST`请求：会给服务器提交一些数据或者文件。
3. 在`Flask`中，`route`方法，默认将只能使用`GET`的方式请求这个url，如果想要设置自己的请求方式，那么应该传递一个`methods`参数。

## 重定向

重定向分为永久重定向和暂时性重定向，在页面上体现的操作就是浏览器会从一个页面自动跳转到另一个页面，

1. 永久性重定向：`http`的状态码是301，多用于旧网址被废弃了要转到新的网址确保用户的访问，最经典的就是京东网站
2. 暂时性重定向：`http`的状态码是302，表示页面的暂时性跳转。比如访问一个需要权限的网址，如果当前用户没有登录，应该重定向到登录页面

### flask中的重定向

`flask`中有一个函数叫做`redirect`，可以重定向到指定网站。

```python
from flask import Flask, request, redirect, url_for
app = Flask(__name__)

@app.route('/login/')
def login():
    return '这是登陆页面'

@app.route('/profile/')
def profile():
    if request.args.get('name'):
        return '个人中心页面'
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
```

## 模板预热

1. 在渲染模板的时候，默认会从项目根目录下的`templates`目录下查找
2. 如果不想把模板文件放在`templates`目录下，那么可以在`Flask`初始化的时候指定`template_folder`来指定模板路径。

## 模板参数

1. 在使用`render_template`渲染模板的时候，可以传递关键字参数，以后直接在模板中使用就可以。
2. 如果你的参数过多，可以将所有参数放入字典中，使用`**context`选择要传递的参数。

## url_for

模板中的`url_for`和后台视图函数的使用方法基本一样，也是传递视图函数的名字，也可以传递参数。使用的时候，要在两天加`{{}}`。

## 过滤器

### 什么是过滤器，语法是什么

1. 过滤器是通过管道符号`|`进行使用的，例如：`{{name|length}}`，将返回name的长度。过滤器相当于是一个函数，把当前的变量传入到过滤器中，然后过滤器根据自己的功能，在返回相应的值，之后再将结果渲染到页面中。
2. 基本语法：`{{variable|过滤器名字}}`。使用管道符号进行分割

### 常用过滤器

#### `default`过滤器

使用方式`{{value|default('默认值')}}`。如果`value`这个`key`不存在，那么就会使用`default`过滤器提供的默认值。如果你想使用类似与`python`中判断一个值是否为Flase，那么久必须要传递另外一个参数`{{value|default('默认值', boolean=True)}}`。或者使用`{{signature|'此人很懒')}}`。

#### 自动转义过滤器

1. `safe`过滤器：可以关闭一个字符串的自动转义

2. `escape`过滤器：对某一个字符串进行转义

3. `autoescape`标签，可以对他里面的代码块关闭/开启自动转义

   ```jinja2
   {% autoescape off %}
   代码
   {% endautoescape %}
   ```

### 自定义模板过滤器

过滤器本质上就是一个函数。如果在模板中调用这个过滤器，那么就会将这个变量的值作为第一个参数传递给过滤器这个函数，然后函数的返回值会作为这个过滤器的返回值。需要使用到装饰器。

```python
@app.template_filter('my_cut')
def cut(value):
    value = value.replace('hello','')
    return value
```

## if条件判断语句

`if`条件判断语句必须放在`{% %}`中间，并且必须有结束的标签`{%endif%}`。和`python`中的类似，可以使用条件判断来进行判断，也可以通过`and, or, not`来进行逻辑操作。

## for循环

在`jinja2`中的`for`循环，跟`python`中的`for`循环基本上是一样的，也是`for...in`的形式。并且可以遍历所有的序列以及迭代器。但是唯一不同的是，`jinja2`中的`for`循环没有`break`和`continue`语句。

## 宏

模板中的宏跟python中的函数类似，可以传递参数，但是不能有返回值，可以将一些经常用到的代码片段放到宏中，然后把一些不固定的值抽取出来当成一个变量。使用宏的时候，参数可以为默认值。

1. 定义宏

   ```html
   {% macro input(name,value="",type="text") %}
       <input type="{{ type }}" name="{{ name }}" value="{{ value }}">
   {% endmacro %}
   ```

2. 使用宏

   ```html
   {{ input("password", type="password") }}
   {{ input(value="提交", type="submit") }}
   ```

### 导入宏

1. `import`宏的路径
2. `from`宏文件的路径`import`宏的名字`as xxx`
3. 宏文件路径，不要以相对路径去寻找，都要以`templates`作为绝对路径去找
4. 如果想要在导入宏的时候，就把当前模板的一些参数传递给宏所在的模板，那么应该使用`with context`

## include

1. 这个标签相当于是直接将制定的模板中的代码复制到当前位置。
2. `include`标签，如果想要使用父模板中的变量，直接用就可以，不需要使用`with context`。
3. `include`的路径，也是跟`import`一样，直接从`templates`根目录下去找，不要以相对路径找。

## set、with语句

### set语句

在模板中，可以使用`set`语句来定义变量。

```html
{% set username="zhiliao" %}
<p>用户名：{{ username }}</p>
```

一旦定义了这个变量，那么在后面的代码中，都可以使用这个变量，就类似于Python的变量定义时一样的。

### with语句

`with`语句定义的变量，只能在`with`语句中使用，超过这个代码块就不能使用。

```html
{% with classroom="zhiliao1班" %}
    <p>班级：{{ classroom }}</p>
{% endwith %}
```

`with`语句不一定要跟一个变量，可以定义一个空的`with`语句，以后在`with`块中通过`set`定义的变量，就只能在这个`with`块中使用。

```html
{% with  %}
	{% set classroom="zhiliao1班" %}
    <p>班级：{{ classroom }}</p>
{% endwith %}
```

## 静态文件

1. 加载静态文件使用的是`url_for`函数，然后第一个参数需要为`static`，第二个参数需要为一个关键字参数`filename=路径`.

   ```html
   {{ url_for('static', filename='imgs/scrapy.png') }}
   ```

   路径查找，要以当前项目的static目录作为根目录。

## 模板继承

### 为什么需要模板继承

模板继承可以把一些公用的代码单独抽取出来放到一个父模板中，以后子模板直接继承就可以使用。这样可以减少重复性，修改比较方便。

### 模板继承语法

使用`extends`语句，来指明继承的父模板。父模板的路径，也是相对于`templates`文件夹下的绝对路径。

`{% extends "base.html" %}`

### block语法

一般在父模板中，定义一些公共的代码。子模板可能要根据具体的需求实现不同的代码。这时候父模板就应该有能力提供一个接口，让父模板来实现。从而实现具体业务需求的功能。

在父模板中：

```html
{% block body_block %}
{% endblock %}
```

在子模板中：

```html
{% block body_block %}
    我是body block中的代码
{% endblock %}
```

### 调用父模板代码block中的代码

默认情况下，子模板如果实现了父模板定义的block。那么子模板block中的代码就会覆盖父模板中的代码。如果想要在子模板中仍然保留父模板中的代码，那么可以使用`{{ super() }}`。

父模板：

```html
{% block body_block %}
	<p style="background: red">我是block中的代码</p>
{% endblock %}
```

子模板：

```html
{% block body_block %}
    {{ super() }}
    <p style="background: green">我是子模板中的代码</p>
{% endblock %}
```

### 调用另外一个block中的代码

如果想要在另外一个模板中使用其他模板中的代码，那么可以通过`{{self.其他block名字()}}`。

```python
{% block body_block %}
    {{ self.title() }}
    <p style="background: green">我是子模板中的代码</p>
{% endblock %}
```

### 请他注意事项

1. 子模板中的代码，第一行应该是`extends`。继承应该放在第一行。
2. 子模板中，如果要实现自己的代码，应该放到block中，放在其他地方不会被渲染。