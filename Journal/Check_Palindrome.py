# Write a program to determine if a given string is palindrome or not using combination of positive and negative
# indexing. Take the string as an input from the user.

class checkPalindrome:
    def __init__(self, s):
        self.s = s

    def palindromeCheck(self):  # method to check if the entered string is palindrome or not
        self.s = self.s.lower()  # converts the entered input into lowercase
        isPalindrome = True  # flag variable initially set to True
        length = len(self.s) // 2  # we take half the length of input since we need to match first half with second half
        for i in range(length):
            if self.s[i] != self.s[-(i + 1)]:
                # if the first and second half don't match, we make isPalindrome to False, thus indicating not a palindrome
                isPalindrome = False
        if isPalindrome:
            return "Palindrome"
        else:
            return "Not a palindrome"


string = input("Enter a string: ")   # takes input from the user
p = checkPalindrome(string)  # object creation
print(p.palindromeCheck())  # function call
