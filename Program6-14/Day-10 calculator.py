# # functions with outputs
# def format_name(fname, lname):
#     fname = fname.upper()
#     lname = lname.upper()
#     return fname + " " +lname
#
#
#
#
# title_name = format_name("sunil", "appanna")
#
# print(title_name)

# doubt
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print("Leap year.")
#             else:
#                 print("Not leap year.")
#         else:
#             print("Leap year.")
#     else:
#         print("Not leap year.")
#
#
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) == "Not Leap year":
#         print(29)
#     return month_days[month - 1]
#
#
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


# def addition(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1 - n2
#
# def division(n1, n2):
#     return n1 + n2
#
# def multiply(n1, n2):
#     return n1 + n2
#
# operations = {
#   "+": addition,
#   "-": subtract,
#   "*": multiply,
#   "/": division
# }
#
# num1 = int(input("enter the first number: "))
# for symbol in operations:
#     print(symbol)
# operation_symbol = input("pick an operation in above: ")
# num2 = int(input("enter the second number: "))
# calculation_function = operations[operation_symbol]
# answer = calculation_function(num1, num2)
#
# print(answer)


from art import calculator_logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(calculator_logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
