# -*- coding: utf-8 -*-
# @Time     : 2019/12/24 13:15
# @Author   : 童庆
# @FileName : 3.turtle画五星红旗.py
# @Software : PyCharm


'''
在开始绘制之前，我们要明白一点：不是随手画出的五星红旗都是国旗。
在我国，国旗的形状、大小是有明确规定的，
根据《中华人民共和国国家标准 国旗（GB 12982-2004）》，
这份标准明确记录了国旗的比例、颜色、每颗星的形状和位置等信息，为我们绘制国旗提供参考。
百度百科：
https://baike.baidu.com/item/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E5%9B%BD%E6%97%97/240342
'''

'''
画五星红旗思路：
1.首先画红色背景
2.根据国旗制定标准计算出五角星坐标
    大五角星：-175，145
    第一个小五角星：-100,180
    第二个小五角星：-85,150
    第三个小五角星：-85,120
    第四个小五角星：-100，-100
3.先画大五角星，再画小五角星
4.forward默认是朝东开始画，setheading可以调整初始朝向角度
'''

# 导入turtle模块
import turtle

# 设置画图的速度
turtle.speed(2)
# 抬起笔，移动坐标，设定初始坐标
turtle.up()
turtle.goto(-200, 200)
# 放下笔准备画
turtle.down()
# 准备填充颜色
turtle.begin_fill()
# 设置填充色和画笔的颜色
turtle.fillcolor('red')
turtle.pencolor('red')
# 使用循环，循环两次画出一个矩形
for i in range(2):
    turtle.forward(438)
    turtle.right(90)
    turtle.forward(292)
    turtle.right(90)
# 完成颜色填充
turtle.end_fill()

# 设置五角星颜色
turtle.fillcolor('yellow')
turtle.pencolor('yellow')

# 画大五角星
turtle.up()
turtle.goto(-170, 145)
turtle.down()
turtle.begin_fill()
for i in range(5):
    turtle.forward(50)
    turtle.right(144)
turtle.end_fill()

# 画第一颗小五角星
turtle.up()
turtle.goto(-100, 180)
# 调整画第一条线的角度
turtle.setheading(305)
turtle.down()
turtle.begin_fill()
for i in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()

# 画第二颗小五角星
turtle.up()
turtle.goto(-85, 150)
turtle.setheading(30)
turtle.down()
turtle.begin_fill()
for i in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()

# 画第三颗小五角星
turtle.up()
turtle.goto(-85, 120)
turtle.setheading(3)
turtle.down()
turtle.begin_fill()
for i in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()

# 画第四颗小五角星
turtle.up()
turtle.goto(-100, 100)
turtle.setheading(300)
turtle.down()
turtle.begin_fill()
for i in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()
# 隐藏箭头
turtle.hideturtle()
turtle.done()

turtle.mainloop()