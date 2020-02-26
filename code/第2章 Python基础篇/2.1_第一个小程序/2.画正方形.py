# -*- coding: utf-8 -*-
# @Time     : 2019/12/24 11:22
# @Author   : 童庆
# @FileName : 2.turtle画正方形.py
# @Software : PyCharm

# 导入turtle
import turtle
# 设置画笔的粗细为4，颜色为红色,速度为1
turtle.pensize(4)
turtle.pencolor('red')
turtle.speed(1)
# 向右画，长度为100
turtle.forward(100)
# 顺时针转90度
turtle.right(90)
# 向下画，长度为100
turtle.forward(100)
# 顺时针转90度
turtle.right(90)
# 向上画，长度为100
turtle.forward(100)
# 顺时针转90度
turtle.right(90)
# 向右画，长度为100
turtle.forward(100)

# 循环执行，关掉画图窗口执行后面的程序
turtle.mainloop()