year = int(input('enter the year: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('LEAP YEAR')
        else:
            print('NOT A LEAP YEAR')
    else:
        print('LEAP YEAR')
else:
    print('NOT A LEAP YEAR')