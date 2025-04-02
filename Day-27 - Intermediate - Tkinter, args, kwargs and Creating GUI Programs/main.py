from tkinter import *

window = Tk()
window.title("my first gui program")
window.minsize(height=500, width=500)




label = Label(text="New name", font=("roboto", 24, "bold"))
label.pack()


label["text"] = "my New text"
label.config()


def buttonClicked():
    my_text = input.get()
    label["text"] = my_text


button = Button(text="click me", command=buttonClicked)
button.pack()



input = Entry()
input.pack()




window.mainloop()









# import tkinter
#
# window = tkinter.Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
#
# # Label
#
# my_label = tkinter.Label(text="I Am a Label", font=("roboto", 24, "bold"))
# my_label.pack()
#
# my_label["text"] = "New Text"
# my_label.config(text="New Text")
#
#
# # Buttone
# def button_clicked():
#     print("I got clicked")
#     new_text = input.get()
#     my_label.config(text=new_text)
#
#
# button = tkinter.Button(text="click me", command=button_clicked)
# button.pack()
#
# # Entry
# input = tkinter.Entry()
# input.pack()
#
# # import turtle
# #
# # tim = turtle.Turtle()
# # tim.write("some text")
#
#
#
# window.mainloop()
