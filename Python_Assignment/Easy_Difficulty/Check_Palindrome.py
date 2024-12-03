class check_Palindrome:
    def __init__(self, string):
        self.string = string

    def checkPalindrome(self):  # function to check whether a string is a palindrome or not
        self.string = self.string.lower()  # converts the entered string into lowercase
        reverse_string = self.string[::-1]  # reverse the string using slicing
        if self.string == reverse_string:  # check if reversed_string matches the original string
            print("Palindrome")
        else:
            print("Not palindrome")


string = input("Enter a string: ")  # takes user input
s = check_Palindrome(string)  # object creation
s.checkPalindrome()  # function call

