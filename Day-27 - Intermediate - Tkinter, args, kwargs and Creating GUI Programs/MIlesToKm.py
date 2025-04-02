from tkinter import *


def km_calculate():
    miles = float(miles_input.get())
    km = round(miles * 1.689)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("MILES TO KM")
window.minsize(height=400, width=400)
window.config(padx=40, pady=40)

miles_input = Entry()
miles_input.grid(row=0, column=3)

miles_labels = Label(text="Miles")
miles_labels.grid(row=0, column=4)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=2)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(row=1, column=3)

kilometer_label = Label(text="KM")
kilometer_label.grid(row=1, column=4)

calculate_button = Button(text="Calculate", command=km_calculate)
calculate_button.grid(row=2, column=3)

window.mainloop()
