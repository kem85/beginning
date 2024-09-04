import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Palestinian Flag")
screen.bgcolor("white")

# Set up the turtle
flag = turtle.Turtle()
flag.speed(3)
flag.color("black")
flag.begin_fill()
for _ in range(35):
    flag.right(10)
    flag.forward(20)
flag.
flag.end_fill()
flag.hideturtle()

# Keep the window open
turtle.done()