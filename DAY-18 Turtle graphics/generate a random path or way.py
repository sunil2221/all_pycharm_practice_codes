import turtle as t
import random

tim = t.Turtle()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 360]

tim.pensize(15)  # thickness of the line
tim.speed("fastest")  # change the moving speeds of line


for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(direction))
