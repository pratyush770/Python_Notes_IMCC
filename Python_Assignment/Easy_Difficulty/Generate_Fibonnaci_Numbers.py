class generate_Fibonnaci_Numbers:
    def __init__(self, n):
        self.n = n
    def printFibonnaciNumbers(self):  # function to print the first 10 Fibonacci numbers
        n1 = 0  # n1 variable initialized to 0
        n2 = 1  # n1 variable initialized to 1
        print(f"The fibonacci numbers for the first {self.n} numbers are:", n1, n2, end=" ")
        for i in range(2, self.n):  # generate the remaining fibonacci numbers
            n3 = n1 + n2
            print(n3, end=" ")
            n1 = n2
            n2 = n3
