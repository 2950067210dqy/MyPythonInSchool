import turtle
import random
def randomcolor():
    colorArr = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ""
    for i in range(6):
        color += colorArr[random.randint(0,15)]
    return "#"+color
for i in range(100):
	turtle.hideturtle()
	x=random.randrange(-200,200)
	y=random.randrange(-200,200)
	turtle.up()
	turtle.goto(x,y)
	turtle.down()
	turtle.color(randomcolor())
	turtle.begin_fill()
	for j in range(3):
	turtle.end_fill()
	# turtle.bgcolor(randomcolor())
