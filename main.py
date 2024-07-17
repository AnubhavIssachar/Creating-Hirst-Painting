#import colorgram
import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.hideturtle()
screen = Screen()
color_list = [(214, 154, 105), (49, 96, 139), (163, 80, 45), (223, 209, 107), (17, 36, 59), (185, 163, 25),
              (120, 163, 202), (56, 30, 18), (126, 68, 94), (210, 91, 69), (43, 128, 70), (193, 140, 160),
              (162, 20, 10), (125, 181, 156), (58, 28, 40), (129, 26, 42), (19, 52, 43), (194, 91, 113), (48, 170, 98),
              (39, 62, 97), (27, 91, 52), (235, 162, 187), (108, 118, 172), (225, 206, 2), (6, 88, 108),
              (227, 179, 170), (65, 81, 31), (140, 214, 195), (170, 183, 217), (54, 146, 192), (165, 203, 213)]
dot_size = 20
gap = 50
rows = 10
columns = 10
tim.width(6)
x = 120
y = 80
turtle.colormode(255)
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for i in range(columns):
    for _ in range(rows):
        tim.penup()
        tim.dot(dot_size, random.choice(color_list))
        tim.forward(gap)
    if i % 2 == 0:
        tim.left(90)
        tim.forward(gap)
        tim.left(90)
        tim.forward(gap)
    else:
        tim.right(90)
        tim.forward(gap)
        tim.right(90)
        tim.forward(gap)

# rgb_colors = []
# colors = colorgram.extract("hirstp.jpg", 100)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
screen.exitonclick()
