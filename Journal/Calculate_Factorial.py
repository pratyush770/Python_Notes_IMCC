# Without using readymade methods, write a program to find factorial of a given number.
# Take the number from the user.

class calculateFact:
    def __init__(self, num):
        self.num = num
    def calculateFactorial(self):  # method to calculate the factorial of a number
        fact = 1
        for i in range(1, self.num + 1):
            fact = fact * i
        print(f"The factorial of {self.num} is {fact}")


n = int(input("Enter a number: "))   # takes input from the user
f = calculateFact(n)
f.calculateFactorial()  # function call
