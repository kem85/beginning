import turtle
screen = turtle.Screen()
screen.title("Palestinian Flag")
screen.bgcolor("white")
flag = turtle.Turtle()
flag.speed(5000)
flag.color("black")
flag.begin_fill()
for _ in range(35):
    flag.right(10)
    flag.forward(20)
flag.end_fill()
flag.goto(-150, 50)
flag.begin_fill()
for _ in range(35):
    flag.right(10)
    flag.forward(20)
flag.end_fill()
flag.penup()
flag.goto(-70,-10)
flag.pendown()
flag.begin_fill()
flag.left(50)
count = 1
    for _ in range(90):
        count += 1
        if count < 40:
            flag.left(3)
        flag.forward(5)
        if count < 70:
            flag.right(2)
        else:
            flag.left(5)
        flag.right(3)
        flag.end_fill()
flag.penup()
flag.goto(80,60)
flag.pensize(20)
flag.pendown()
flag.end_fill()
flag.color("white")
flag.right(20)
flag.forward(10)
flag.end_fill()
flag.hideturtle()
turtle.done()