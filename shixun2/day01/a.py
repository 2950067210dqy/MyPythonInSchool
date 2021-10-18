#coding:utf-8
import turtle as t
t.setup(800,600)
t.pensize(5)
#画笔类型
t.shape('arrow')
t.shapesize(2,2,1)
t.color('red','red')
#画图速度
t.speed(8)
t.begin_fill()
t.left(140)
t.forward(112)
for i in range(200):
    t.right(1)
    t.forward(1)
t.left(120)
for i in range(200):
    t.right(1)
    t.forward(1)
t.forward(112)
t.end_fill()
#原点位置在正中间
t.penup()
t.goto(70,50)
t.pendown()
t.setheading(0)
t.begin_fill()
t.left(140)
t.forward(112)
for i in range(200):
    t.right(1)
    t.forward(1)
t.left(120)
for i in range(200):
    t.right(1)
    t.forward(1)
t.forward(112)
t.end_fill()
t.penup()
t.goto(-150,30)
t.pendown()
t.pensize(15)
t.setheading(0)
t.left(30)
t.forward(450)
t.done()
