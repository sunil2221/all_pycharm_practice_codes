import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========= 
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6
word_list = ["apple", "ball", "cat", "dog"]
chosen = random.choice(word_list)
print(chosen)
word_length = len(chosen)


display = []
for _ in range(word_length):
    display += "_"
end_game = True
while end_game:

    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen:
        lives -= 1
        if lives == 0:
            end_game = False
            print("lose")
    print(display)

    if "_" not in display:
        end_game = False
        print("you win")
    print(stages[lives])

