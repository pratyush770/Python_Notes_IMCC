# Q1) Write a Python program to demonstrate the use of basic arithmetic operators (+, -, *, /).
# num1 = int(input("Enter the first number: "))   # takes user input
# num2 = int(input("Enter the second number: "))
# print(f"The addition of {num1} and {num2} is {num1 + num2}")  # adds two numbers using (+) arithmetic operator
# if num1 > num2:
#     print(f"The subtraction of {num1} and {num2} is {num1 - num2}")  # subtracts two numbers using (-) arithmetic operator
# else:
#     print(f"The subtraction of {num1} and {num2} is {num2 - num1}")
# print(f"The multiplication of {num1} and {num2} is {num1 * num2}")  # multiplies two numbers using (*) arithmetic operator
# if num1 > num2:
#     print(f"The division of {num1} and {num2} is {num1 / num2}")  # divides two numbers using (/) arithmetic operator
# else:
#     print(f"The division of {num1} and {num2} is {num2 / num1}")


# Q2) Create a program that converts a given Celsius temperature to Fahrenheit.
# def celsiusToFahrenheit(celsius):
#     f = (9/5) * celsius + 32  # formula to convert Celsius into Fahrenheit
#     print(f"The temperature in Celsius {celsius} after converting to Fahrenheit is {f}")
#
#
# cel = int(input("Enter the temperature in Celsius: "))
# celsiusToFahrenheit(cel)  # function call


# Q3) Write a Python script to declare and access values in a list.
# mylist = []  # create an empty list
# n = int(input("Enter the number of elements you want to insert in the list: "))
# for i in range(n):
#     inp = int(input("Enter the value to add in the list: "))
#     mylist.append(inp)  # append the elements in the list
# print(f"The list is as follows: {mylist}")  # print the entire list
# print(f"The first element in the list is {mylist[0]}")  # access the first element from the list


# Q4) Define a dictionary with at least 3 key-value pairs and retrieve a value using its key.
# student = {  # create a dictionary with 4 key-value pairs
#     "name": "Pratyush",
#     "age": 20,
#     "clg": "IMCC",
#     "phone": 7666234983
# }
# print(f"The name of the student is {student["name"]}")  # retrieves the name of the student using the key
# print(f"The college of the student is {student["clg"]}")  # retrieves the college of the student using the key


# Q5) Use list comprehension to create a list of squares for numbers 1 to 10.
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # list holding values from 1 to 10
# res = [val ** 2 for val in mylist]  # list comprehension to generate square of each number from the list
# print(res)


# Q6) Write a program that checks if a number is even or odd using an if statement.
# num = int(input("Enter a number: "))
# if num % 2 == 0:  # check if the entered number is even
#     print(f"The number {num} is an even number")
# else:  # check if the entered number is odd
#     print(f"The number {num} is an odd number")


# Q7) Create a Python function to find the maximum of three numbers.
# def findMaxNum(num1, num2, num3):  # function to find the maximum of three numbers
#     if num1 > num2 and num1 > num3:  # check if the first number is the maximum among the three numbers
#         print(f"The maximum number is {num1}")
#     elif num2 > num1 and num2 > num3:  # check if the second number is the maximum among the three numbers
#         print(f"The maximum number is {num2}")
#     else:  # check if the third number is the maximum among the three numbers
#         print(f"The maximum number is {num3}")
#
#
# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# n3 = int(input("Enter the third number: "))
# findMaxNum(n1, n2, n3)


# Q8) Write a Python program that reads a text file and prints its content line by line.
# f = open("file.txt", 'r')  # opens the specified file in read mode
# try:
#     for file in f:
#         print(file.strip())  # reads each content line by line and removes extra whitespaces
# except FileNotFoundError:  # if file not found
#     print("File not found..")


# Q9) Create a program to count the number of characters in a string provided by the user.
# string = input("Enter the string: ")  # asks the user for string input
# string = string.lower()  # converts the entered string into lowercase
# ch = input("Enter the character: ")  # asks the user for character to check the occurence
# count = 0
# for s in string:
#     if s == ch:
#         count += 1
# print(f"The occurence of character {ch} is {count}")  # prints the occurence of characters in the string


# Q10) Define a simple class in Python and create an object of that class.
# class Student:  # creates a class named Student
#     def __init__(self, name, age, phone):  # initializes a constructor and accepts 3 parameter
#         self.name = name  # public attributes
#         self.age = age
#         self.phone = phone
#
#     def printDetails(self):  # method to print the entered details
#         print(f"The name of the student is {self.name}")
#         print(f"The age of the student is {self.age}")
#         print(f"The phone number of the student is {self.phone}")
#
#
# n = input("Enter the name of the student: ")  # takes user input
# a = int(input("Enter the age of the student: "))
# p = int(input("Enter the phone number of the student: "))
# s = Student(n, a, p)  # create an object of Student class and pass the arguments
# s.printDetails()  # call the printDetails method


# Q11) Write a Python function that accepts a list and returns its reverse.
# def reverseList(list):  # function to reverse a list
#     revlist = list[::-1]  # reverses the list using slicing
#     print(f"The list after reversing is {revlist}")  # prints the reversed list
#
#
# mylist = [1, 2, 3, 4, 5]  # list holding 5 elements
# reverseList(mylist)  # call the reverseList method


# Q12) Use a for loop to print the first 10 Fibonacci numbers.
# n1 = 0  # n1 variable initialized to 0
# n2 = 1  # n2 variable initialized to 1
# print("The fibonacci series for the first 10 numbers are:", n1, n2, end=" ")  # print n1 and n2 initially
# for i in range(2, 10):  # use for loop to generate the remaining fibonacci numbers
#     n3 = n1 + n2
#     print(n3, end=" ")
#     n1 = n2
#     n2 = n3


# Q13) Write a Python program to append text to a file and then display its content.
# f = open("file.txt", "r")  # opens the file in read mode
# print("The content of file before appending is...")
# print(f.read())  # displays the content of file before appending
# f = open("file.txt", "a")  # opens the file in append mode
# f.write(" This text gets appended")  # this text gets appended
# f = open("file.txt", "r")  # opens the file in read mode
# print("The content of file after appending is...")
# print(f.read())   # displays the content of file after appending


# Q14) Implement a function to check whether a string is a palindrome.
# def checkPalindrome(string):  # function to check whether a string is a palindrome or not
#     string = string.lower()  # converts the entered string into lowercase
#     rev_string = string[::-1]  # reverses the string using slicing
#     if rev_string == string:  # check if reversed string matches the actual string
#         print("The entered string is palindrome")
#     else:
#         print("The entered string is not palindrome")
#
#
# mystring = input("Enter a string: ")  # takes the user input
# checkPalindrome(mystring)  # function call


# Q15) Demonstrate the use of a while loop by printing numbers from 1 to 10.
# n = 1  # n variable initialized to 1
# while n <= 10:  # will execute from 1 to 10
#     print(n, end=' ')  # prints the numbers
#     n += 1  # increments the number by 1 after printing each number
