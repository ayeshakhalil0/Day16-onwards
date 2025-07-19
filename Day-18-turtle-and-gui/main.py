import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
# tim.color("red")

color_list =  ["red","green","blue","black","orange","purple","pink","yellow"]
directions = ["up","down","forward","backward"]
# shape creation
# for i in range(3,10):
#     angle = 360
#     tim.color(random.choice(color_list))
#     for j in range(i):
#         tim.forward(50)
#         tim.right(angle/i)

# random walk
# tim.speed("fastest")
turtle.colormode(255)
#
# tim.pensize(10)
# for i in range(200):
#     tim.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#     choice = random.choice(directions)
#     if choice == "forward":
#         tim.forward(20)
#     elif choice == "backward":
#         tim.backward(20)
#     elif choice == "down":
#         tim.right(90)
#     else:
#         tim.left(90)

# circle

tim.speed("fastest")
for _ in range(int(360/5)):
    tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.circle(60)
    # tim.tilt(30)
    tim.setheading(tim.heading() + 5)


screen = Screen()
screen.exitonclick()

# import heroes
# print(heroes.gen())