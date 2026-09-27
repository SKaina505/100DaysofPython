import random
import turtle
from turtle import Turtle, Screen

from main import screen

#Code to make turtle move forward on click of space bar
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()

#Code to create Make an Etch A Sketch App
tim = Turtle()
display = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def clock_wise():
    tim.right(10)

def anti_clock_wise():
    tim.left(10)

def clear_drawing():
    tim.reset()



display.listen()
display.onkey(key="w",fun=move_forward)
display.onkey(key="s",fun=move_backward)
display.onkey(key="d",fun=clock_wise)
display.onkey(key="a",fun=anti_clock_wise)
display.onkey(key="c",fun=clear_drawing)

display.exitonclick()
