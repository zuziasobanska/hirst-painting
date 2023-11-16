import turtle

from turtle import Turtle, Screen
import random
paintbrush = Turtle()
paintbrush.shape("turtle")
paintbrush.color("green")

turtle.colormode(255)

colour_list = [(233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162)]

random_colour = random.choice(colour_list)

paintbrush.speed("fastest")
def make_drawing():
    paintbrush.hideturtle()
    current_position = -200
    paintbrush.penup()
    paintbrush.setposition(-200, current_position)
    for _ in range(10):
        for _ in range(10):
            random_colour = random.choice(colour_list)
            paintbrush.dot(20, random_colour)
            paintbrush.penup()
            paintbrush.forward(50)
        current_position += 50
        paintbrush.setposition(-200, current_position)

make_drawing()

screen = Screen()
screen.exitonclick()