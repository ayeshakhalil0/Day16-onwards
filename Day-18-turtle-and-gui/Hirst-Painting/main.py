# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpeg', 30)
#
# for items in colors:
#     rgb_colors.append((items.rgb.r,items.rgb.g,items.rgb.b))
#
# print(rgb_colors)

# above is for extracting colors from images
from turtle import Turtle, Screen
import turtle
import random

tim = Turtle()
tim.shape("triangle")
turtle.colormode(255)
tim.speed(20)

color_list  = [(198, 159, 116), (70, 92, 129), (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45), (100, 160, 85), (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23), (219, 206, 8)]

for _ in range(10):
    for _ in range(10):
        tim.dot(10,random.choice(color_list))
        tim.penup()
        tim.forward(20)
    tim.setheading(90)
    tim.forward(20)
    tim.setheading(180)
    tim.forward(200)
    tim.setheading(0)


screen = Screen()
screen.exitonclick()
