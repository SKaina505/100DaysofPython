import random
import turtle
from turtle import Turtle, Screen

#Code to make a racing turtle bet game

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y_position = [-70,-40,-10,20,50,80]
all_turtles = []

#My code to create five turtle with diffrent color and diffrent positions for the race
# def create_turtle(col,y):
#     tim = Turtle(shape="turtle")
#     tim.color(col)
#     tim.penup()
#     tim.goto(x=-230, y=y)
#
# for color in colors:
#     position = random.randint(a=-100,b=100)
#     create_turtle(col=color,y=position)

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
