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