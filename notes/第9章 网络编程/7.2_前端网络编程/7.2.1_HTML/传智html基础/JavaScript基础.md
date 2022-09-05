# JavaScript基础

---

## JavaScript的介绍

### JavaScript的定义

JavaScript是运行在浏览器端的脚本语言，是由浏览器解释执行的，检查js。它能够让网页和用户有交互功能，增加良好的用户体验效果。

前端开发三大模块：

1. HTML：负责网页结构
2. CSS：负责网页样式
3. JavaScript：负责网页行为

## JavaScript的使用方式

1. 行内式（主要用于事件）

2. 内嵌式

3. 外链式

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <!-- 内嵌式 -->
    <script>
        alert("我是内嵌式的js代码");
    </script>

    <!-- 外链式 -->
    <script src="js/main.js"></script>
</head>
<body>
    <!-- 行内式 -->
    <input type="button" value="按钮" onclick="alert('你点我了')">
</body>
</html>
```

```js
alert('我是外链式的js代码');
```

## 变量和数据类型

### 定义变量

JavaScript是一种弱类型语言，也就是说不需要指定变量的类型，JavaScript的变量类型由它的值来决定，定义变量需要用关键字`var`，一条JavaScript语句应该以`;`结尾。

定义变量的语法格式：

`var 变量名 = 值;`

### JavaScript注释

`单行注释 //  多行注释 /* */ `

### 数据类型

![JavaScript数据类型](D:\repository\PythonNotes\notes\第7章 网络编程\images\JavaScript数据类型.png)

### 变量命名规范

1. 区分大小写
2. 第一个字符必须是字母，下划线或者美元符号
3. 其他字符可以是字母，数字，下划线或美元符号

### 匈牙利命名风格

![匈牙利命名风格](D:\repository\PythonNotes\notes\第7章 网络编程\images\匈牙利命名风格.png)

## 函数定义和调用

### 函数定义

函数就是可以重复使用的代码块，使用关键字`function`定义函数。

### 函数的基本使用

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script>
        // 定义函数的关键字 function
        function fnShow(){
            alert('我是一个无参数无返回值的函数');
        }

        // 调用函数
        fnShow()

        // 定义有参数有返回值的函数
        function fnSum(iNum1, iNum2){
            var iResult = iNum1 + iNum2;
            return iResult;
            alert('测试代码');
        }

        var iNum = fnSum(1, 2);
        alert(iNum)
        // return关键字的特点：
        // 1.可以为函数提供返回值 2.当执行return语句以后函数执行结束，后面的代码不会再执行
    </script>
</head>
<body>
    
</body>
</html>
```

## 变量作用域

### 变量作用域的介绍

变量作用域就是变量的使用范围，变量分为：

- 局部变量
- 全局变量

### 局部变量和全局变量

局部变量是函数内部使用的变量，而全局变量在函数外定义的变量，可以在不同函数内使用，并且不同函数内可以共享变量。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script>
        function fnShow(){
            // 局部变量
            var iNum = 1;
            alert(iNum);
        }
        fnShow()

        // 全局变量：在函数外定义的变量，可以在不同函数内使用，并且不同函数内可以共享变量
        var iNum1 = 1;

        function fnModify(){
            alert(iNum1);
            iNum1 = 3;
            // ++ 等价于 += 1
            iNum1 ++
            iNum1 += 1
            alert(iNum1);
        }
        fnModify()
        // js可以数字类型和字符串之间直接相加，把数字自动转成字符串
        alert("函数外的全局变量：" + iNum1)
    </script>
</head>
<body>
    
</body>
</html>
```

