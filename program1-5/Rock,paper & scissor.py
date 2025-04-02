import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) '''
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? type 0 for Rock, 1 for paper or 2 for scissor:  "))
if 3 <= user_choice < 0:
    print("you type valid number")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print(game_images[computer_choice])
    print(f"computer choice is: {computer_choice}")

    if user_choice == 0 and computer_choice == 2:
        print("you win")

    elif user_choice == 2 and computer_choice == 0:
        print("computer win, you lose ")
    elif computer_choice > user_choice:
        print("computer win, you lose")
    elif user_choice > computer_choice:
        print("you win")
    elif computer_choice == user_choice:
        print("it's Draw")
