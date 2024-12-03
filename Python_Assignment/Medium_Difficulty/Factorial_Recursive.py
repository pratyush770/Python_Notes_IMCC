class recursive_Factorial:  # function to calculate factorial of number using recursion
    def calculateFactorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.calculateFactorial(n - 1)  # logic to calculate factorial using recursion


n = int(input("Enter the number: "))  # takes user input
r = recursive_Factorial()  # object creation
print(r.calculateFactorial(n))  # function call
