# CSS基础

---

## CSS定义

CSS(Cascading Style Sheet)层叠样式表，它是用来美化页面的一种语言。

## CSS作用

1. 美化页面，比如：设置标签文字大小、颜色、字体加粗等样式
2. 控制页面布局，比如：设置浮动，定位等样式

## CSS的引入方式

### 行内式

`<div style="width:100px; height:100px; background: red;">hello</div>`

优点：方便直观；缺点：缺乏可重用性

### 内嵌式

```html
<head>
    <style type="text/css">
        h3{
            color:gray
        }
    </style>
</head>
```

优点：在同一个页面内部便于复用和维护；缺点：在多个页面之间的可重用性不高

### 外链式

> 将CSS代码写在一个单独的`.css`文件里，在`<head>`标签中使用`<link>`标签直接引入改文件到页面中。

`<link rel="stylesheet" href="css/main.css">`

优点：是的css样式和html页面分离，便于整个页面系统的维护和规划，可重用性高。缺点：css代码由于分离到单独的css文件，容易出现css代码过于集中，若维护不当则极容易造成混乱。

### 具体使用

```css
h1{
    color: skyblue;
}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 内嵌式 -->
    <style>
        /* css 里面的注释：ctrl + / */
        /* 选择器给标签添加样式 */
        a{
            color: green;
        }
    </style>

    <!-- 外链式 -->
    <link rel="stylesheet" href="css/main.css">
</head>
<body>
    <!-- 行内式 -->
    <p style="color: red">我是一个段落标签</p>

    <a href="https://www.baidu.com">百度</a>

    <h1>我是一级标题</h1>
</body>
</html>
```

## CSS选择器

### CSS选择器的定义

用来选择标签的，选出来后给标签加样式

### CSS选择器的种类

1. 标签选择器
2. 类选择器
3. 层级选择器
4. id选择器
5. 组选择器
6. 伪类选择器

### 实例应用

#### 标签选择器

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        p{
            color: red;
        }
    </style>
</head>
<body>
    <!-- 标签选择器，就是以标签名开头，根据标签名来选择html文件中的标签，给标签添加样式 -->
    <p>hello world</p>
</body>
</html>
```

#### 类选择器

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        /* 类选择器，以·开头，根据类名选择标签，给标签添加样式 */
        .myp{
            color: red;
        }
        .mypg{
            background: green;
        }
    </style>
</head>
<body>
    <p>我是一个标签</p>
    <p class="myp">哈哈，我是一个段落标签</p>
    <!-- 这里的标签使用了两个类选择器 -->
    <p class="myp mypg">哈哈，我是一个段落标签</p>
</body>
</html>
```

#### 层级选择器

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        /* 层级选择器要有层级关系，根据层级关系获得子标签，给子标签添加样式 */
        div div{
            color: green;
        }
        div .box2{
            color: blue;
        }
        div p{
            color: aqua;
        }
    </style>
</head>
<body>
    <div>
        <div>哈哈</div>
        <div class="box2">嘻嘻</div>
    </div>
    <div>哈哈</div>
    <!-- 层级选择器不一定必须是父子关系，祖孙关系的子标签也可以找到，完成添加样式的操作 -->
    <div>
        <div>
            <p>hello</p>
        </div>
    </div>
</body>
</html>
```

#### id选择器

根据id选择标签，以#开头，元素的id名不能重复，所有id选择器只能对应于页面上的一个元素不能复用，id名一般给程序使用，所有不推荐使用id作为选择器。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        #myid1{
            color: blue;
        }
    </style>
</head>
<body>
    <p id="myid1">呵呵</p>
</body>
</html>
```

#### 组选择器

多个选择器的一个组合

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        .box1, .box2, .box3{
            width: 100px;
            height: 100px;
        }
        .box1{
            background: red;
        }
        .box2{
            background: green;
        }
        .box3{
            background: blue;
        }
    </style>
</head>
<body>
    <!-- div.box1*3：创建3个div并且指定class属性的名字是box1 -->
    <div class="box1"></div>
    <div class="box2"></div>
    <div class="box3"></div>
</body>
</html>
```

#### 伪类选择器

用于向选择器添加特殊效果

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        div{
            width: 100px;
            height: 100px;
            background: green;
        }
        /* 伪类选择器就是个其他选择器添加效果，表现形式是选择器后面加上冒号 */
        div:hover{
            width: 200px;
            height: 200px;
            background: red;
        }
    </style>
</head>
<body>
    <div>和哈</div>
</body>
</html>
```

## CSS属性

### 布局常用样式属性

![CSS布局常用属性](D:\repository\PythonNotes\notes\第7章 网络编程\images\CSS布局常用属性.png)

#### 实例

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .box{
            width: 100px;
            height: 100px;
            background: green;
            /* 设置背景图片，no-repeat不重复图片 */
            /* background: url("1.png") no-repeat; */
            /* 设置标签的四周边框 */
            border: 5px solid red;
            /* 设置浮动 */
            /* float: right; */
        }

        .box1{
            width: 200px;
            height: 200px;
            background: blue;
        }
        .box2{
            width: 50px;
            height: 50px;
            background: green;
            float: left;
        }
        .box3{
            width: 50px;
            height: 50px;
            background: red;
            /* 设置div在一行显示 */
            float: left;
        }
    </style>
</head>
<body>
    <!-- 布局常用控件 div -->
    <div class="box">哈哈</div>
    <br>
    <!-- div>div*2 创建一个父div在父div里面创建两个字div -->
    <div class="box1">
        <div class="box2"></div>
        <div class="box3"></div>
    </div>
</body>
</html>
```

### 文本常用属性

![CSS文本常用属性](D:\repository\PythonNotes\notes\第7章 网络编程\images\CSS文本常用属性.png)

#### 实例

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        p{
            color: red;
            font-size: 30px;
            font-weight: bold;
            font-family: "Microsoft Yahei";
            background: pink;
            text-decoration: underline;
            /* 设置行高，适合上下居中 */
            line-height: 50px;
            /* 设置居中 */
            text-align: center;
            /* 设置文本缩进 */
            /* text-indent: 30px; */
        }

        span{
            color: green;
        }

        a{
            /* 取消下划线 */
            text-decoration: none;
        }
    </style>
</head>
<body>
    <!-- span可以给文本中选定内容设置样式 -->
    <p>听说下雨天，音乐和<span>辣条</span>更配</p>
    <a href="https://www.baidu.com">百度</a>
</body>
</html>
```

## CSS元素溢出

### 什么是css元素溢出

当子元素的尺寸超过父元素的尺寸时，此时需要设置父元素显示溢出的子元素的方式。设置的方法是通过overflow属性来完成。

overflow的设置项：

1. visiable默认值，显示子标签溢出部分
2. hidden隐藏子标签溢出部分
3. auto如果子标签溢出，则可以滚动查看其余的内容

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        .box1{
            width: 100px;
            height: 100px;
            background: red;
            /* 设置元素溢出需要在父标签中设置 */
            /* auto超出部分滚动显示 */
            /* overflow: auto; */
            overflow: hidden;
        }

        .box2{
            width: 200px;
            height: 50px;
            background: green;
        }
    </style>
</head>
<body>
    <div class="box1">
        <div class="box2"></div>
    </div>
</body>
</html>
```

## CSS显示特性

### display属性的使用

display属性是用来设置元素的类型及隐藏的，常用的属性有：

- none元素隐藏且不占位置
- inline元素以行内元素显示
- block元素以块元素显示

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        .box1{
            width: 100px;
            height: 100px;
            background: red;
            /* 把该标签隐藏并且不占用位置 */
            display: none;
        }
        .box2{
            /* width: 100px;
            height: 100px; */
            background: red;
            /* 可以设置div与其他元素在一行显示，但是不能设置宽高 */
            /* 以后即设置div的宽高，又设置在一行显示可以通过浮动来完成 */
            display: inline;
        }

        a{
            /* 设置标签自己单独占一行，不和其他标签在一行显示 */
            display: block;
        }
    </style>
</head>
<body>
    <div class="box1">
        哈哈
    </div>
    <p>嘻嘻</p>
    <div class="box2">
        哈哈
    </div>
    <a href="https://www.baidu.com">百度</a>
</body>
</html>
```

## 盒子模型

### 盒子模型的介绍

所谓的盒子模型就是把HTML页面的元素看做一个矩形盒子，矩形盒子是由内容（content），内边距(padding)，边框(border)，外边框（margin）四部分组成。

盒子示意图如下：

![盒子示意图](D:\repository\PythonNotes\notes\第7章 网络编程\images\盒子示意图.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        .box1{
            width: 200px;
            height: 200px;
            background: green;
            border: 5px solid blue;
            padding-top: 10px;
        }

        .box2{
            width: 100px;
            height: 150px;
            background: red;
        }

        .box3{
            width: 50px;
            height: 50px;
            background: gray;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <!-- 盒子模型主要设置4部分内容，
        1.内容大学（width, height）
        2.边框大小（border） 
        3.内边距大小（padding）
        4.外边距大小（margin）-->
    <div class="box1">
        <div class="box2"></div>
    </div>
    <div class="box3"></div>
</body>
</html>
```

