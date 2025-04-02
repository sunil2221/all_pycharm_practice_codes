import turtle as t    # t is a alias name that name is re-defined

# # tim = turtle.Turtle() # this is one way
tim = t.Turtle()  # alias name using


for _ in range(20):
    tim.forward(10)
    tim .penup()
    tim.forward(10)
    tim.pendown()

