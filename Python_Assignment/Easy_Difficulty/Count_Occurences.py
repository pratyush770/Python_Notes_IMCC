class count_Occurences:
    def __init__(self, str, ch):
        self.str = str
        self.ch = ch

    def countOccurences(self):  # function to count the occurences of character in the string
        self.str = self.str.lower()  # converts the entered input into lowercase
        self.ch = self.ch.lower()  # converts the entered input into lowercase
        count = 0
        for i in self.str:
            if i == self.ch:
                count += 1
        return count


str = input("Enter the string: ")  # takes user input
ch = input("Enter the character: ")
s = count_Occurences(str, ch)  # object creation
print(s.countOccurences())  # function call


