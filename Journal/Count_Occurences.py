# Without using count() demonstrate the use of for loop to determine the number of occurences of a given
# character in a string. Take the string and character from the user.

class countOccurences:
    def __init__(self, s, ch):
        self.s = s
        self.ch = ch

    def occurencesOfChar(self):  # method to check the occurences of character in a string
        count = 0
        for i in self.s:
            if i == self.ch:  # if the occurence of character matches the index, we increment the count
                count += 1
        return count


s = input("Enter a string: ")   # takes input from the user
ch = input("Enter a character: ")
c = countOccurences(s, ch)  # object creation
print(c.occurencesOfChar())  # function call
