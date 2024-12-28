# Without using any readymade methods, write a program in Python to reverse the sequence of words in a given string.
# Take the string from the user.

class reverseWords:
    def __init__(self, s):
        self.s = s

    def reverseWords(self):  # method to reverse the sequence of words in a string
        st = self.s.split()  # splits the words and creates a list
        reverse_str = st[::-1]  # reverse the order of words using indexing
        output = ' '.join(reverse_str)  # joins all the reverse words
        return output


s = input("Enter a string: ")   # takes input from the user
r = reverseWords(s)
print(r.reverseWords())  # function call
