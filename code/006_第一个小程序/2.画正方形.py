# -*- coding: utf-8 -*-
# @Time     : 2019/12/24 11:22
# @Author   : 童庆
# @FileName : 2.turtle画正方形.py
# @Software : PyCharm

# 在使用函数时，如果不是内置函数，首先需要进行导入
import turtle

# 设置画笔的粗细和颜色
turtle.pensize(4)
turtle.pencolor('red')

# forward 表示向前
# right 表示向右转90度
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.mainloop()