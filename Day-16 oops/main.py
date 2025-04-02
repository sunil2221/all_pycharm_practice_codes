# import another_module
# print(another_module.value)
#
# from turtle import Turtle, Screen
#
# my_screen = Screen()
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemom", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "c"
print(table)


