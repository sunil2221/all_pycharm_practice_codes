alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo_CC

print(logo_CC)


# def encrypt(plan_text,  shift_amount):
#     cipher_text = ""
#     for letter in plan_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#
#     print(f"the encrypt text is {cipher_text}")
#
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for char in cipher_text:
#         position = alphabet.index(char)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#
#     print(f"decrypt message : {plain_text}")
#
#
# if direction == "encode":
#     encrypt(plan_text=text, shift_amount=shift)
# else:
#     decrypt(cipher_text=text, shift_amount=shift)


# simplest way
def ceaser(ceaser_text, shift_amount, ceaser_direction):
    end_text = ""
    if ceaser_direction == "decode":
        shift_amount *= -1
    for char in ceaser_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"the {ceaser_direction}d text in: {end_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    ceaser(ceaser_text=text, shift_amount=shift, ceaser_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_continue = False
        print("Goodbye")
