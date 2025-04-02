size = input('enter the size of pizza? S, M OR L: ').lower()
pepper = input('you want pepper "Y" or "N" : ').lower()
cheese = input('you want extra cheese "Y" or "N" : ').lower()
bill = 0
if size == 's':
    bill += 15
elif size == 'm':
    bill += 20
else:
    bill += 25



if pepper == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3

if cheese == 'y':
    bill += 1

print(f'your final bill is {bill}')
