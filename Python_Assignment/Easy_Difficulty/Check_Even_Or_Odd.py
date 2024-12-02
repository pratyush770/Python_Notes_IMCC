class check_Even_Or_Odd:
    def __init__(self, n):
        self.n = n
    def checkEvenOrOdd(self):  # function to check if number is even or odd
        if self.n % 2 == 0:  # checks if number is even
            print(f"The number {self.n} is an even number")
        else:  # checks if number is odd
            print(f"The number {self.n} is an odd number")

