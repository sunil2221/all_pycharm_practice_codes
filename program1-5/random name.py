import random

names = input("Enter your names:  ").split(",")
num_of_items = len(names)
random_choice = random.randint(0, num_of_items - 1)
random_name = names[random_choice]

print(f"{random_name} is going to buy a meal today")

