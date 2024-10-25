# This file contains all the string methods

# 1) Write a program to determine if a given string is palindrome or not using combination of positive and negative
# indexing. Take the string as an input from the user.
def palindromeCheck(s):  # method to check if the entered string is palindrome or not
    s = s.lower()  # converts the entered input into lowercase
    isPalindrome = True  # flag variable initially set to True
    length = len(s) // 2  # we take half the length of input since we need to match first half with second half
    for i in range(length):
        if s[i] != s[-(i + 1)]:
            # if the first and second half don't match, we make isPalindrome to False, thus indicating not a palindrome
            isPalindrome = False
    if isPalindrome:
        print("Palindrome")
    else:
        print("Not a palindrome")


# 2) Without using count() demonstrate the use of for loop to determine the number of occurences of a given
# character in a string. Take the string and character from the user.
def occurencesOfChar(s, c):  # method to check the occurences of character in a string
    count = 0
    for i in s:
        if i == c:  # if the occurence of character matches the index, we increment the count
            count += 1
    print(count)


# 3) Without using any readymade methods, write a program in Python to reverse the sequence of words in a given string.
# Take the string from the user.
def reverseWords(string):  # method to reverse the sequence of words in a string
    st = string.split()  # splits the words and creates a list
    reverse_str = st[::-1]  # reverse the order of words using indexing
    output = ' '.join(reverse_str)  # joins all the reverse words
    print(output)
