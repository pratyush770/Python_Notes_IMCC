# This file contains all the integer methods

# 1) Without using readymade methods, write a program to find factorial of a given number.
# Take the number from the user.
def calculateFactorial(num):  # method to calculate the factorial of a number
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print(f"The factorial of {num} is {fact}")


# 2) Without using any readymade methods, write a program in Python to check if the given number is an
# Armstrong number or not. Take the number from the user.
def armstrongCheck(num):  # method to check if the number is armstrong or not
    temp = num  # temporary variable which holds same value as the entered input
    sum = 0
    rem = 0
    while num > 0:
        rem = num % 10
        sum = sum + (rem * rem * rem)
        num = num // 10
    if sum == temp:
        print(f"{temp} is an Armstrong number")
    else:
        print(f"{temp} is not an Armstrong number")
