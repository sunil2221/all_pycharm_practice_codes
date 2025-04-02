from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("welcome to the password generator")
    letters_chose = random.randint(8, 10)
    numbers_choice = random.randint(2, 4)
    symbols_choice = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(letters_chose)]
    password_numbers = [random.choice(numbers) for _ in range(numbers_choice)]
    password_symbols = [random.choice(symbols) for _ in range(symbols_choice)]

    password_list = password_letters + password_numbers + password_symbols

    password_gen = "".join(password_list)
    password_entry.insert(0, password_gen)
    pyperclip.copy(password_gen)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="please make sure you haven't left any fields empty.")
    # else:
    #     is_ok = messagebox.askyesno(title="website",
    #                                 message=f"these are the details entered: \n Email: {email} \n password: {password} \n Is it ok to save?")

    else:
        with open("data.json", "r") as data_file:
            json.dump(new, data_file, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

my_canvas = Canvas(height=200, width=200)
p_img = PhotoImage(file="logo.png")
logo = my_canvas.create_image(100, 100, image=p_img)
my_canvas.grid(row=0, column=1)

my_label = Label(text="Website: ")
my_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

my_label = Label(text="Email/Password:")
my_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "sunil1213@gmail")

my_label = Label(text="Password:")
my_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_pwd_btn = Button(text="Generate Password", command=password_generator)
generate_pwd_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
