# Python Notes - IMCC
# *** Syntax error will not execute the program whereas Logical error will execute but will show incorrect output ***

# import sys
# import random as r
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


# String literal and type_casting
# 1) x = 10
# st1 = 'Allowed'  # string value in single quotes
# _st2 = "allowed"  # string value in double quotes
# ST1 = "Case Sensitive"  # ST1 is different from st1
# print(f"Value of x is {x}")
# print(f"Value of st1 is {st1}")
# print(f"Value of _st2 is {_st2}")
# print(f"Value of ST1 is {ST1}")
# x = "reassignment"  # operator overloading
# print(f"Reassigned value is {x}")

# 2) y = 10
# val_int = int(y)  # type_cast to int
# val_float = float(y)  # type_cast to float
# val_str = str(y)  # type_cast to string
# print(f"The value of val_int is {val_int}")
# print(f"The value of val_float is {val_float}")
# print(f"The value of val_str is {val_str}")

# 3) v1, v2, v3 = 10.00, 20.50, 12.75
# sum = v1 + v2 + v3
# print(f"The sum of all the variables is {sum}")  # format method
# print(type(sum))  # provides the variable data type

# 4) num1 = 20
# num2 = 30
# st1 = "Hello"
# st2 = "World"
# print(num1)  # 20
# print(num2)  # 30
# print(num1 + num2)  # 50 i.e. addition operation(int + int)
# print(st1)  # Hello
# print(st2)  # World
# print(st1 + st2)  # HelloWorld i.e. concatenation(str + str)
# print(st1, st2)  # Hello, World
# print(num1, st1)  # 20, Hello
# print(num1 + st1)  # Will throw error since int + str is not possible


# Practice Program
# You are making a housie game app to generate random numbers. Write a python program to help you get these numbers
# 6 times for a given housie ticket
# for i in range(6):  # 0,5 is the range
#     num = r.randint(1, 100)  # randint() generates random number between the specified range
#     print(num, end=' ')


# If-elif-else
# 1) age = int(input("Enter your age : "))
# if age < 18:
#     print("You are not an adult yet")
# elif age == 18:
#     print("Just 18!")
# else:
#     print("Legally adult")

# 2) age = int(input("Enter your age : "))
# print("You are not an adult yet" if age < 18 else "Just 18!" if age == 18 else "Legally adult")  # ternary operator


# Switch control(match)
# day = input("Enter the day of the week : ")
# day = day.lower()
# match day:  # match keyword is similar to switch keyword in other programming languages
#     case 'monday' | 'mon':
#         print("Monday")
#     case 'tuesday' | 'tue':
#         print("Tuesday")
#     case 'wednesday' | 'wed':
#         print("Wednesday")
#     case 'thursday' | 'thu':
#         print("Thursday")
#     case 'friday' | 'fri':
#         print("Friday")
#     case 'saturday' | 'sat':
#         print("Saturday")
#     case 'sunday' | 'sun':
#         print("Sunday")
#     case _:  # for default case, will always come at the end
#         print("Enter a valid day of the week")


# Loops in python
# while(True):  # infinite loop
#     num = int(input("Enter a number : "))
#     if num % 2 == 0:
#         print(f"The entered number {num} is an even number")
#         continue
#     else:
#         print(f"The entered number {num} is an odd number")
#         break
# print("This line will execute only if the entered number is odd")


# Practice Program
# val = int(input("Enter the number : "))
# primeSt = False
# for i in range(2, (val//2)+1):
#     if val % i == 0:
#         break
#     else:
#         primeSt = True
# if(primeSt):
#     print(f"The entered number {val} is a prime number")
# else:
#     print(f"The entered number {val} is not a prime number")


# File Handling
# 1) Read operations in file
# f = open('file.txt')  # default mode is 'r'
# print(f.read())  # read method is used to display the contents of the file
# print(f.read(10))  # will read only first 10 characters
# print(f.tell())  # method to get the file pointer's current position
# f.seek(22)  # method to move the file pointer to a specific position
# print(f.read())
# print(f.readline())  # will only read the first line
# print(f.readlines())  # will read all the lines and display in the form of a list
# Alternative way to print all the lines instead of readlines()
# f.seek(0)
# for line in f:
#     print(line)

# 2) Write operations in file
# f = open('file.txt', 'w')  # will open in 'w' mode
# f.write('The first line got overwritten\n')  # will overwrite the content
# f.write('The second line got overwritten')
# f.writelines(['The first line got overwritten\n', 'The second line got overwritten'])  # writes multiple lines and expects the data in the form of a list
# f.close()
# f = open('file.txt')
# print(f.read())

# 3) f = open('file.txt', 'a')  # will open in 'a' mode
# f.write('This line gets appended')  # appends the text in front of the already existing text
# f.close()
# f = open('file.txt')
# print(f.read())


# List
# monthNames = list(("Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"))
# n = int(input("Enter any number between 1 to 12: "))
# print("The month corresponding to the given number is:", monthNames[n - 1])  # n - 1 since indexing starts from 0
# daysOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# print(daysOfWeek[:3])  # will display the list elements from 0:2 i.e. Mon, Tue, Wed
# daysOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# print(daysOfWeek[3:])  # will display the list elements from 3:end i.e. Thu, Fri, Sat, Sun
# rainfallData = [[1, "Arunachal Pradesh", 5], [2, "Sikkim", 1], [3, "West Bengal", 4], [4, "Odisha", 2], [5, "Uttarakhand", 3]]  # Multi dimensional list
# print(rainfallData[4][0], rainfallData[4][1], rainfallData[4][2])


# Dictionary
# myDictionary = {1: "Apple", 2: "Cherry", 3: "Banana", 4: "Peach"}
# print(myDictionary)
# print(f"The length of the dictionary is {len(myDictionary)}")
# studentRecord = {"name": "ABC",
#                  "age": 20,
#                  "contactNumbers": [123456, 987653],
#                  "blood_type": "B+"}
# print(studentRecord)
# print(studentRecord["name"])
# print(studentRecord["contactNumbers"])
# print(type(studentRecord))
# studentRecord = {"name": "ABC",
#                  "age": 20,
#                  "contactNumbers": [123456, 987653]}
# oneMoreStudentRecord = studentRecord  # copy of above dictionary
# print(f"The new dictionary looks like: {oneMoreStudentRecord}")
# studentRecord.update({"address": "Mumbai"})
# print(f"Modified studentRecord dictionary looks like: {studentRecord}")
# print(f"The new dictionary looks like: {oneMoreStudentRecord}")   # this copy dictionary gets updated too


# Tuples
# myTuple = ("Pratyush", )  # one element with comma indicates a tuple
# print(type(myTuple))
# firstTuple = ()  # empty tuple
# print('First tuple', firstTuple)
# print(type(firstTuple))
# secondTuple = ("mon", "tue", "wed", "thu")  # string elements
# print("Second tuple", secondTuple)
# print(type(secondTuple))
# thirdTuple = (1, 2, 3)  # int elements
# print(f"Third tuple {thirdTuple}")
# print(type(thirdTuple))
# fourthTuple = ("fri", "sat", "sun")  # string elements
# print(f"Fourth tuple {fourthTuple}")
# print(type(fourthTuple))
# fifthTuple = (secondTuple, thirdTuple)  # nested tuple and allows heterogeneous elements
# print(f"Fifth tuple {fifthTuple}")
# print(type(fifthTuple))
# myList = [10, 20, 30]
# sixthTuple = tuple(myList)  # adding the list as an element to the tuple
# print(f"Sixth tuple {sixthTuple}")
# seventhTuple = (90)  # is considered an int not as a tuple. It is a logical error since the code will work.
# print(f"Eighth tuple {seventhTuple}")
# print(type(seventhTuple))
# eightTuple = tuple(range(10, 0, -1))  # will print the numbers from 10-1 in form of a tuple
# print(f"Ninth tuple {eightTuple}")

# Unpacking tuples in a variable
student = ("ABC", 24, "Mumbai")
print(f"Student tuple looks like this {student}")
name, age, city = student  # unpacking student tuple
print(f"The name of the students is {name}, age is {age} and city is {city}")
# Use of asterisk in unpacking a tuple
one, two, *other, three = (1, 2, 3, 4, 5)
print(f"One: {one}")
print(f"Two: {two}")
print(f"Three: {three}")
print(f"All: {other}")



