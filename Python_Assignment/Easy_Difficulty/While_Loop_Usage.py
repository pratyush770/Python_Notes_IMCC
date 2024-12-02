class while_Loop_Usage:
    def __init__(self, n):
        self.n = n
    def printNumbers(self):  # function to print numbers from 1 to 10 using while loop
        num = 1  # variable named n initialized to 1
        while num <= self.n:  # will execute from 1 to entered number
            print(num, end=' ')
            num += 1  # keep incrementing after every print

