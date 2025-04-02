from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
coffee_maker.report()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f'what would you like? {options}')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        my_money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = my_money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)
