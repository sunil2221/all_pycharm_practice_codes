print("welcome to the tip calculator.")

bill = float(input("what was the bill : "))
tip = int(input("what percentage of tip would you like to give ? 10, 15, 20: "))
tip_percent = tip/100
tip_amount = bill * tip_percent
total_bill = bill + tip_amount

no_of_person = int(input("how many person to split the bill: "))
split = round(total_bill / no_of_person, 2)

print(f"Each person should pay : {split}")
print(total_bill)


# print("welcome to the tip calculator.")
#
# bill = float(input("what was the bill : "))
# tip = int(input("what percentage of tip would"
#                 " you like to give ? 10, 15, 20: "))
#
# total_bill = bill + tip
#
# no_of_person = int(input("how many person to split the bill: "))
# split = round(total_bill / no_of_person, 2)
#
# print(f"Each person should pay : {split}")
# print(total_bill)


# my own // wrong
# print("Welcome to the tip calculator\n")
# bill = float(input("what was the total bill: \n"))
# tip_percent = int(input("what percentage tip would you like to give ? 10,12,15 "))
# peoples = int(input("how many people to split the bill: "))
# total_tip = (tip_percent/100) * bill
# total_bill = bill + total_tip
# split_bill = round(total_bill/7, 2)
# print(f"each person have to the {split_bill}")