# 1) Write a program to determine if a given string is palindrome or not using combination of positive and negative indexing. Take the string as an input from the user.
# string = input("Enter a string: ")   # takes input from the user
# string = string.lower()   # converts the entered input into lowercase
# isPalindrome = True   # flag variable initially set to True
# length = len(string) // 2   # we take half the length of input since we need to match first half with second half
# for i in range(length):
#     if string[i] != string[-(i + 1)]:  # if the first and second half don't match, we make isPalindrome to False, thus indicating not a palindrome
#         isPalindrome = False
# if isPalindrome:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

#2) Without using count() demonstrate the use of for loop to determine the number of occurences of a given character in a string. Take the string and character from the user.
# string = input("Enter a string: ")   # takes input from the user
# ch = input("Enter a character: ")
# count = 0
# for i in string:
#     if i == ch:   # if the occurence of character matches the index, we increment the count
#         count += 1
# print(count)

# 3) Without using readymade methods, write a program to find factorial of a given number. Take the number from the user.
# n = int(input("Enter a number: "))   # takes input from the user
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(f"The factorial of {n} is {fact}")

# 4) Without using any readymade methods, write a program in Python to reverse the sequence of words in a given string. Take the string from the user.
# s = input("Enter a string: ")   # takes input from the user
# string = s.split()   # splits the words and creates a list
# reverse_str = string[::-1]   # reverse the order of words using indexing
# output = ' '.join(reverse_str)   # joins all the reverse words
# print(output)

# 5) Without using any readymade methods, write a program in Python to check if the given number is an Armstrong number or not. Take the number from the user.
# n = int(input("Enter a number: "))   # takes input from the user
# temp = n   # temporary variable which holds same value as the entered input
# sum = 0
# rem = 0
# while n > 0:
#     rem = n % 10
#     sum = sum + (rem * rem * rem)
#     n = n // 10
# if sum == temp:
#     print(f"{temp} is an Armstrong number")
# else:
#     print(f"{temp} is not an Armstrong number")
