import turtle
def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
def main():
    turtle.setup(800,400)
    turtle.speed(1000000000)
    turtle.penup()
    turtle.goto(-100,-50)
    turtle.pendown()
    turtle.pensize(2)
    level=5
    koch(50,level)
    turtle.right(120)
    koch(50,level)
    turtle.right(120)
    koch(50,level)
    turtle.hideturtle()
main()