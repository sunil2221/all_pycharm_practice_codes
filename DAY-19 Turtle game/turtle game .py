from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading()-10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.home()


screen.listen()
screen.onkey(move_forward, "w")  # this is one way
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
