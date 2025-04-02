# BMI CALCULATOR 2.0

Height = float(input("enter your height in m: "))
Weight = int(input("enter your weight in kgs: "))

bmi_cal = Weight / Height ** 2
print(bmi_cal)

bmi = int(bmi_cal)

if bmi <= 18.5:
    print("under weight")
elif 18.5 <= bmi <= 25:
    print("normal weight")
elif 25 <= bmi <= 30:
    print("over weight")
elif 30 < bmi <= 35:
    print("obese weight")

else:
    print("clinically obese")
print(bmi)
