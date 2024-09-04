import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Palestinian Flag")
screen.bgcolor("white")

# Set up the turtle
flag = turtle.Turtle()
flag.speed(500)
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
flag.begin_fill()
flag.right(70)
for _ in range(1500):
    flag.forward(15)
    flag.right(1)
flag.end_fill()



# # Function to draw a rectangle
# def draw_rectangle(color, width, height):
#     flag.color("black")
#     flag.pensize(0)
#     flag.begin_fill()
#     for _ in range(2):
#         flag.forward(width)
#         flag.right(90)
#         flag.forward(height)
#         flag.right(90)
#         flag.fillcolor(color)
#     flag.end_fill()
# # Function to draw the triangle
# def draw_triangle(color, base, height):
#     flag.pensize(0)
#     flag.pensize(0.1)
#     flag.begin_fill()
#     flag.forward(base)
#     flag.left(135)
#     flag.forward(height)
#     flag.left(90)
#     flag.forward(height)
#     flag.left(135)
#     flag.fillcolor(color)
#     flag.end_fill()

# # Draw the flag
# flag.penup()
# flag.goto(-150, 100)
# flag.pendown()

# # Black stripe
# draw_rectangle("black", 300, 50)

# # Move to position for white stripe
# flag.penup()
# flag.goto(-150, 50)
# flag.pendown()

# # White stripe
# draw_rectangle("white", 300, 50)

# # Move to position for green stripe
# flag.penup()
# flag.goto(-150, 0)
# flag.pendown()

# # Green stripe
# draw_rectangle("green", 300, 50)

# # Move to position for red triangle
# flag.penup()
# flag.goto(-150, 100)
# flag.setheading(270)  # Point downward
# flag.pendown()

# # Red triangle
# draw_triangle("red", 150, 106.07)  # The height is calculated based on the Pythagorean theorem
# Hide the turtle
flag.hideturtle()

# Keep the window open
turtle.done()