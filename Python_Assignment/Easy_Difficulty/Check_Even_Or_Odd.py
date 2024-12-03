class check_Even_Or_Odd:
    def __init__(self, n):
        self.n = n

    def checkEvenOrOdd(self):  # function to check if number is even or odd
        if self.n % 2 == 0:  # checks if number is even
            print("Even number")
        else:  # checks if number is odd
            print(f"Odd number")


n = int(input("Enter the number: "))  # takes user input
num = check_Even_Or_Odd(n)  # object creation
num.checkEvenOrOdd()  # function call
