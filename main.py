###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import turtle

import colorgram
from turtle import Turtle,Screen
import random
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

tim = Turtle()
screen = Screen()
turtle.colormode(255)
tim.hideturtle()
tim.speed("fastest")
tim.penup()
tim.seth(225)
tim.forward(300)
tim.seth(0)


color_list = [(149, 75, 50), (222, 201, 136),
              (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149),
              (14, 98, 70), (232, 176, 165),
              (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
              (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


def random_color(list):
    return random.choice(color_list)


def draw_row():
    for i in range(10):
        tim.color(random_color(color_list))
        tim.dot(20)
        tim.forward(50)


def return_home():
    tim.backward(500)


def move_up():
    tim.seth(90)
    tim.forward(50)
    tim.seth(0)


for _ in range(10):
    draw_row()
    return_home()
    move_up()


screen.exitonclick()
