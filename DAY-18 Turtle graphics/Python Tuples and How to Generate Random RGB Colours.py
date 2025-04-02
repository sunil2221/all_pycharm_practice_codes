import turtle as t    # t is alias name that name is re-defined
import random
# tim = turtle.Turtle() # this is one way
tim = t.Turtle()  # alias name using

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


direction = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")


for _ in range(200):
    tim.color(random_color())
    tim.forward(10)
    tim.setheading(random.choice(direction))
