# wall paint calculation
# import math
#
#
# def paint_calc(height, width, cover):  # sample_program
#     area = height * width
#     num_of_cans = math.ceil(area / cover)
#     print(f"you'll need {num_of_cans} cans of paint.")
#
#
# test_h = int(input("enter your height : "))
# test_w = int(input("enter your width: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)
#
#
# # more than one input
# def greet(name, location):  # sample_program-2
#     print(f"hello{name}")
#     print(f"what is like in {location}")
#
#
# # keyword parameter is a assign variable
# greet(name="jack bauer", location="nowhere")


# prime_number_checker
def prime_number(number):  # sample_program-3
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False



    if is_prime:
        print("this is prime number")
    else:
        print("this is not a prime number")


n = int(input("enter the number : "))
prime_number(number=n)
