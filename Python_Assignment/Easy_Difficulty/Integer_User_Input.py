from Arithmetic_Operators_Usage import Arithmetic_Operators_Usage  # import class
from Celsius_To_Fahrenheit import Celsius_To_Fahrenheit
from Declare_And_AccessList import declareAndAccessList
from Check_Even_Or_Odd import check_Even_Or_Odd
from Max_Of_Three_Numbers import find_Max_Number
from Student import student
from Generate_Fibonnaci_Numbers import generate_Fibonnaci_Numbers
from While_Loop_Usage import while_Loop_Usage

# n1 = int(input("Enter the first number: "))  # takes user input
# n2 = int(input("Enter the second number: "))  # takes user input
# ar = Arithmetic_Operators_Usage()  # object creation
# ar.acceptInput(n1, n2)  # function call


# celsius = int(input("Enter the temperature in celsius: "))  # takes user input
# c = Celsius_To_Fahrenheit(celsius)
# c.celsiusToFahrenheit()  # function call

# n = int(input("Enter the number of elements you want to add in the list: "))  # takes user input
# d = declareAndAccessList(n)  # object creation
# d.declareAndAccessList()  # function call

# n = int(input("Enter the number: "))  # takes user input
# num = check_Even_Or_Odd(n)  # object creation
# num.checkEvenOrOdd()  # function call

# n1 = int(input("Enter the first number: "))  # takes user input
# n2 = int(input("Enter the second number: "))
# n3 = int(input("Enter the third number: "))
# num = find_Max_Number(n1, n2, n3)  # object creation
# num.findMaxNumber()  # function call

# name = input("Enter the name of the student: ")  # takes user input
# age = int(input("Enter the age of the student: "))
# phone = int(input("Enter the phone number of the student: "))
# stud = student(name, age, phone)  # object creation
# print()
# stud.printValues()  # function call

# n = int(input("Enter the limit: "))  # takes user input
# fibo = generate_Fibonnaci_Numbers(n)  # object creation
# fibo.printFibonnaciNumbers()  # function call

limit = int(input("Enter the limit: "))
number = while_Loop_Usage(limit)
number.printNumbers()  # function call

