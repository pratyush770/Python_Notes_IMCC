# 1) Write a program to determine if a given string is palindrome or not using combination of positive and negative indexing. Take the string as an input from the user.
# def palindrome(s):
#     s = s.lower()  # converts the entered input into lowercase
#     isPalindrome = True  # flag variable initially set to True
#     length = len(s) // 2  # we take half the length of input since we need to match first half with second half
#     for i in range(length):
#         if s[i] != s[-(i + 1)]:  # if the first and second half don't match, we make isPalindrome to False, thus indicating not a palindrome
#             isPalindrome = False
#     if isPalindrome:
#         print("Palindrome")
#     else:
#         print("Not a palindrome")
#
#
# string = input("Enter a string: ")   # takes input from the user
# palindrome(string)  # function call

#2) Without using count() demonstrate the use of for loop to determine the number of occurences of a given character in a string. Take the string and character from the user.
# def occurences(s, c):
#     count = 0
#     for i in s:
#         if i == c:  # if the occurence of character matches the index, we increment the count
#             count += 1
#     print(count)
#
#
# string = input("Enter a string: ")   # takes input from the user
# ch = input("Enter a character: ")
# occurences(string, ch)  # function call

# 3) Without using readymade methods, write a program to find factorial of a given number. Take the number from the user.
# def factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact = fact * i
#     print(f"The factorial of {num} is {fact}")
#
#
# n = int(input("Enter a number: "))   # takes input from the user
# factorial(n)  # function call

# 4) Without using any readymade methods, write a program in Python to reverse the sequence of words in a given string. Take the string from the user.
# def reverse_words(string):
#     st = string.split()  # splits the words and creates a list
#     reverse_str = st[::-1]  # reverse the order of words using indexing
#     output = ' '.join(reverse_str)  # joins all the reverse words
#     print(output)
#
#
# s = input("Enter a string: ")   # takes input from the user
# reverse_words(s)  # function call

# 5) Without using any readymade methods, write a program in Python to check if the given number is an Armstrong number or not. Take the number from the user.
# def armstrong(num):
#     temp = num  # temporary variable which holds same value as the entered input
#     sum = 0
#     rem = 0
#     while num > 0:
#         rem = num % 10
#         sum = sum + (rem * rem * rem)
#         num = num // 10
#     if sum == temp:
#         print(f"{temp} is an Armstrong number")
#     else:
#         print(f"{temp} is not an Armstrong number")
#
#
# n = int(input("Enter a number: "))   # takes input from the user
# armstrong(n)  # function call

# 6) Without using readline() demonstrate a way in Python to read a multiline file line by line
# def readlines(file):
#     f = open(file)  # opens the specified file in 'r' mode which is default mode
#     f.seek(0)  # starts the file pointer from 0
#     print(f"The contents of {file} are...")
#     for i in f:
#         print(i)  # prints the contents line by line
#
#
# fname = input("Enter the file name: ")
# readlines(fname)

# 7) Using readlines() demonstrate a way to return the total number of NON BLANK lines in a file
# def nonblanklines(file):
#     f = open(file)
#     lines = f.readlines()  # reads all the lines from the specified file
#     count = 0
#     for i in lines:
#         if i.strip():  # removes extra whitespaces thus returning only non-blank lines
#             count += 1
#     print(f"The number of non blank lines in {file} is {count}")
#
#
# fname = input("Enter the file name: ")
# nonblanklines(fname)

# 8) Using file writing methods, write a message from the user in a file. Show use of write when the file is in 'w' mode and 'a' mode
# def writeread(file, msg, ap_msg):
#     f = open(file, 'w')  # opens the specified file in 'w' mode
#     f.write(msg)  # writes the user defined message in the file
#     print("Content written successfully...")
#     f = open(file)
#     print(f.read())  # prints the contents of file after writing
#     print()
#     f = open(file, 'a')  # opens the specified file in 'a' mode
#     f.write(ap_msg)
#     print("Content appended successfully...")
#     f = open(file)
#     print(f.read())
#
#
# fname = input("Enter the file name: ")
# message = input("Enter the message to write in file: ")
# append_msg = input("Enter the message to append after writing: ")
# writeread(fname, message, append_msg)


