# `html`基础

---

## `html`的介绍

### `html`的定义

HTML的全称为：`HyperText Mark-up Language`，指的是超文本标记语言。标记：就是标签，<标签名称></标签名称>，比如：`<html></html> <h1></h1>`等，标签大多数都是成对出现的。

所谓超文本，有两层含义：

1. 因为网页中有图片、视频、语言等内容（超越文本限制）
2. 它还可以在网页中跳转到另一个网页，与世界各地主机的网页链接

### `html`的作用

`html`是用来开发网页的，它是开发网页的语言。

## `html`的基本结构

### 结构代码

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>网页标题</title>
	</head>
	<body>
	</body>
</html>
```

1. 第一行`<!DOCTYPE html>`是文档声明，用来指定页面所用的`html`版本，这里声明的是一个`html5`的文档
2. `<html>...</html>`标签是开发人员告诉浏览器，整个网页是从`<html>`这里开始的，到`</html>`这里结束，也就是`html`文档的开始和结束标签
3. `<head>...</head>`标签用于定义文档的头部，是负责对网页进行设置标题，编码格式以及引入`CSS`和`js`文件的。
4. `<body>...</body>`标签是编写网页上显示的内容

### 实例

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset='utf-8'>
		<title>网页标题</title>
	</head>

	<body>
		<h1>hello world</h1>
	</body>
</html>
```

## 第一个网页

```html
<!DOCTYPE html>
<!-- 注释快捷键 ctrl + / -->
<!-- 当前网页的语言是英文 一般不指定默认为中文 中文为zh -->
<html lang="en">
<head>
    <!-- 指定网页的编码格式 -->
    <meta charset="UTF-8">
    <!-- 在移动设备浏览网页时，网页不缩放 -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    hello
</body>
</html>
```

## 初始常用的`html`标签

```html
<!-- 成对出现的标签 -->
<h1>标题</h1>
<div>div标签</div>
<p>段落标签</p>

<!-- 单个出现的标签 -->
<br>
<img src="" alt="">
<hr>

<!-- 带属性的标签 -->
<img src="" alt="">
<a href=""></a>

<!-- 标签的嵌套 -->
<div>
    <img src="" alt="">
    <a href=""></a>
</div>
```

- 标签不区分大小写，但是推荐使用小写
- 根据标签的书写形式，标签分为双标签和单标签
  - 双标签是指由开始标签和结束标签组成的一队标签，这种标签允许嵌套和承载内容
  - 单标签是一个标签组成，没有标签内容

### 具体使用

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!-- 成对出现的标签 -->
    <h1>我是一级标题</h1>
    <h6>我是六级标题</h6>
    <div>
        我是容器标签，可以包裹其他标签内容
    </div>
    <P>我会段落标签</P>

    <!-- 单标签：只有一个标签，没有标签内容 -->
    <hr>
    <img src="images/1.png" alt="图片加载失败显示的信息">
    <!-- br：换行标签 -->
    <br>

    <!-- 属性标签 -->
    <a href="https://www.baidu.com">百度</a>

    <!-- 标签可以嵌套，不能交叉嵌套 -->
    <div>
        <p>这里是嵌套</p>
    </div>
    
</body>
</html>
```

## 列表标签

列表标签分为无序和有序列表标签

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!-- 无序列表 -->
    <ul>
        <li>苹果</li>
        <li>香蕉</li>
    </ul>

    <!-- 有序列表 -->
    <ol>
        <li>有序1</li>
        <li>有序2</li>
    </ol>
</body>
</html>
```

## 表格标签

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <table style="border: 1px solid black;">
        <tr>
            <th>姓名</th>
            <th>年龄</th>
        </tr>
        <tr>
            <td>张三</td>
            <td>22</td>
        </tr>
    </table>
</body>
</html>
```

## 表单标签

用于搜集不同类型的用户输入的数据，然后把用户数据提交到`web`服务器

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form>
        <p>
            <!-- for 根据id名给指定id的标签设置光标 -->
            <label for="name">用户名：</label>
            <input type="text" id="name">
        </p>
        <p>
            <label>密码：</label>
            <input type="password">
        </p>
        <p>
            <label>性别：</label>
            <input type="radio">男
            <input type="radio">女
        </p>
        <p>
            <label>爱好：</label>
            <input type="checkbox">上课
            <input type="checkbox">睡觉
            <input type="checkbox">打游戏
        </p>
        <p>
            <label>照片：</label>
            <input type="file">
        </p>
        <p>
            <label>个人描述：</label>
            <textarea></textarea>
        </p>
        <p>
            <label>籍贯：</label>
            <select>
                <option>北京</option>
                <option>上海</option>
                <option>安徽</option>
                <option>浙江</option>
            </select>
        </p>
        <p>
            <input type="submit" value="提交">
            <input type="reset" value="重置">
            <input type="button" value="按钮">
        </p>
    </form>
</body>
</html>
```

## 表单提交

`get`方式提交数据到`web`服务器以地址栏的方式提交给服务器不安全，能看到提交的数据。严谨的说是以查询参数的方式提交给`web`服务器。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="https://www.baidu.com" method="POST">
        <p>
            <!-- for 根据id名给指定id的标签设置光标 -->
            <label for="name">用户名：</label>
            <input type="text" id="name" name="username">
        </p>
        <p>
            <label>密码：</label>
            <input type="password" name="password">
        </p>
        <p>
            <label>性别：</label>
            <input type="radio" name="sex" value="0">男
            <input type="radio" name="sex" value="1">女
        </p>
        <p>
            <label>爱好：</label>
            <input type="checkbox" name="hobby" value="2">上课
            <input type="checkbox" name="hobby" value="3">睡觉
            <input type="checkbox" name="hobby" value="4">打游戏
        </p>
        <p>
            <label>照片：</label>
            <input type="file" name="pic">
        </p>
        <p>
            <label>个人描述：</label>
            <textarea name="desc"></textarea>
        </p>
        <p>
            <label>籍贯：</label>
            <select name="position">
                <option value="5">北京</option>
                <option value="6">上海</option>
                <option value="7">安徽</option>
                <option value="8">浙江</option>
            </select>
        </p>
        <p>
            <input type="submit" value="提交">
            <input type="reset" value="重置">
            <input type="button" value="按钮">
        </p>

        <!-- get和post方式提交表单数据都以http协议的方式提交数据给web服务器 -->
    </form>
</body>
</html>
```

