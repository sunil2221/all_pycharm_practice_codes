PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    contents = names_file.readlines()
    print(contents)


with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    # print(letter)
    for name in contents:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        # creating every name with file
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

