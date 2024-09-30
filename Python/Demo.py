# Python Notes - IMCC
# import sys
# print(sys.version)


# if 8>9:
#     print("This statement will execute")
# if 8<9:
#     pass
# print("This statement will execute without any if condition")


# Multi-line comment demonstration
# str = """  -> becomes a variable
# This is a comment sample  -> String literal
# how does it work??
# """
# print("Only this line is executed")
# print(str)


# Scope of variables in python
# 1) Addition of two numbers in python using local variables
# def addition():  # method
#     num1, num2 = 30.50, 40.25  # local variables
#     sumadd = num1 + num2  # local variables
#     print(f"The first number is {num1}")
#     print(f"The second number is {num2}")
#     print(f"Addition of both the numbers is {sumadd}")
# addition()
# print(f"The first number is {num1}")
# # Will not execute and throw NameError since we are accessing local variables outside the function
# print(f"The second number is {num2}")
# print(f"The addition of both the numbers is {sumadd}")

# 2) Addition of two numbers in python using global variables
# num1, num2, sumadd = 30.50, 40.25, 0.0  # global variables
# def addition():  # method
#     print("Inside the addition function")
#     global num1, num2  # made global with the help of global keyword
#     print(f"The first number is {num1}")
#     print(f"The second number is {num2}")
#     num1, num2 = 50.75, 120.25
#     global sumadd  # made global with the help of global keyword
#     sumadd = num1 + num2
#     print(f"Addition of both the numbers is {sumadd}")
# addition()
# print(f"The first number is {num1}")  # will execute since these variables are global
# print(f"The second number is {num2}")
# print(f"The addition of both the numbers is {sumadd}")
