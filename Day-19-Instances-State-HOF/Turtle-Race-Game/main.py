import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)

user_bet = screen.textinput("MAKE YOUR BET","Which turtle will win the race?")
color_list = ["red","orange","yellow","green","blue","purple"]
turtle_objects = []
difference = 0
is_race_on = False


for items in color_list:
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(items)
    new_turtle.goto(-230, -100 + difference)
    difference += 40
    turtle_objects.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_objects:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won")
            else:
                print(f"You lose. Winning color is {winning_color}.")
            is_race_on = False
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()