import turtle as t
import random
#Code to extract colors from an image specifying number of colors
import colorgram

rgb_colors = []
colors = colorgram.extract('images.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)

color = [(7, 14, 38), (29, 16, 13), (180, 144, 132), (120, 97, 61), (233, 210, 87), (213, 84, 69), (76, 8, 19),
         (201, 140, 170), (37, 132, 65), (144, 86, 105), (125, 152, 176), (192, 76, 102), (76, 103, 135),
         (31, 197, 170), (219, 176, 207), (151, 137, 66), (12, 59, 134), (19, 42, 15), (122, 187, 166), (38, 86, 28),
         (123, 9, 26), (87, 132, 174), (11, 217, 225), (133, 222, 208), (240, 204, 9), (232, 173, 168)]
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dot = 100

for dot_count in range(1,number_of_dot + 1):
    tim.dot(15,random.choice(color))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
