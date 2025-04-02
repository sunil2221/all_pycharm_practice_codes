# import colorgram
#
#
# rgb_color = []
# colors = colorgram.extract('hirst spot painting.jpeg', 30)
#
# for color in colors:
#     # rgb_color.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
# print(rgb_color)
#
import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


timmy.color(random_color())
timmy.circle(40)
# current_heading = timmy.heading()
# timmy.setheading(current_heading + 10)


screen = t.Screen()
screen.exitonclick()