def primeChecker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("prime number")
    else:
        print("not a prime number")


n = int(input("enter the number: "))
primeChecker(n)