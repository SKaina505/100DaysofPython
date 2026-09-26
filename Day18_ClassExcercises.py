import turtle
from turtle import Turtle, Screen, Shape
import random

tim = Turtle()
turtle.colormode(255)
tim.speed("fastest")
# Code to get turtle to draw a square
tim.shape("turtle")
tim.color("red")
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)

# Code to get turtle to create a dashed line
for _ in range(15):
    tim.pendown()      # Put the pen down to draw
    tim.forward(10)    # Draw a line segment of 10 pixels
    tim.penup()        # Lift the pen up to stop drawing
    tim.forward(10)    # Move forward 10 pixels without drawing

#Code to get turtle to create shapes
colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]
x = 3
while x < 10:
    angle = 360 / x
    random_color = random.choice(colors)
    tim.color(random_color)
    for num in range(x):
        tim.left(angle)
        tim.forward(100)
    x += 1

#Code to get turtle to do a random walk
colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]
directions = [0,90,180,270]
tim.pensize(15)

for _ in range(100):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))

#Code for random color
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r,g,b)
    return rand_color

#Code for drawing a spirograph

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(10)

screen = Screen()
screen.exitonclick()
