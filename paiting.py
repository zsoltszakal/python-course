import colorgram
import turtle as t
import random

### Get colors from an image
# rgb_colors = []
#
# colors = colorgram.extract('image.jpg', 30)
#
#
# # for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

draw = t.Turtle()
t.colormode(255)

color_list = [(1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20), (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178)]


draw.shape("triangle")
draw.speed("fastest")
draw.penup()
draw.setheading(225)
draw.forward(300)
draw.setheading(0)
number_of_dots = 100
draw.hideturtle()

for dot_count in range(1, number_of_dots + 1):
    draw.dot(20, random.choice(color_list))
    draw.forward(50)

    if dot_count % 10 == 0:
        draw.setheading(90)
        draw.forward(50)
        draw.setheading(180)
        draw.forward(500)
        draw.setheading(0)


screen = t.Screen()
screen.title("Zsolt's Painting")
screen.exitonclick()
