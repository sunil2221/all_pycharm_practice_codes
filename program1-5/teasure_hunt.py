print("welcome to treasure island")
print("your mission is to find the treasure")
direction = input("you've got a cross road, where do you want to go 'left' or 'right':\n ").lower()
if direction == "left":
    task1 = input(
        "you come to a lake. There is an island in the lake. Type 'wait' to wait for a boat. Type 'swim to swim "
        "across' \n").lower()
    if task1 == "wait":
        task2 = input("which door you want to open 'RED' 'YELLOW' OR 'BLUE':").lower()
        if task2 == "yellow":
            print("win")
        else:
            print("Game Over")
    else:
        print("GameOver")
else:
    print("GameOver")