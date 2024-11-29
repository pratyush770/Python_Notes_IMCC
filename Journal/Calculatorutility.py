# Basic arithmetic functions for a calculator
def addition(*num):  # addition function with arbitrary argument
    res = 0
    for n in num:
        res += n
    print(f"The addition of numbers is {res}")


def subtraction(num1, num2):  # subtraction function
    if num1 > num2:
        print(f"The subtraction of numbers is {num1 - num2}")
    else:
        print(f"The subtraction of numbers is {num2 - num1}")


def division(num1, num2):  # division function
    if num1 > num2:
        print(f"The division of numbers is {num1 // num2}")
    else:
        print(f"The division of numbers is {num2 // num1}")


def multiplication(*num):  # multiplication function with arbitrary argument
    res = 1
    for n in num:
        res *= n
    print(f"The multiplication of numbers is {res}")
