age = int(input("what your age: "))

years_remaining = 90 - age
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

print(f"you have {days_remaining} days, {weeks_remaining} weeks,"
      f" and {months_remaining} months are left")
print(f"you have {years_remaining} years are left")
