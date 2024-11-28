# Basic arithmetic functions for a calculator
def addition(num1, num2):  # addition function
    return num1 + num2


def subtraction(num1, num2):  # subtraction function
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1


def division(num1, num2):  # division function
    if num1 > num2:
        return num1 // num2
    else:
        return num2 // num1


def multiplication(num1, num2):  # multiplication function
    return num1 * num2
