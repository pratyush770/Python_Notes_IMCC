class Number:  # class creation
    def __init__(self, n):  # initialize constructor which takes 1 parameter
        self.n = n  # public attribute
    
    def printNumbers(self):  # method to print numbers
        for i in range(1, self.n+1): 
            if i == self.n:  # if we reach at last number
                print(f"Stopped printing at number {i}")
                break  # break out of the loop
            else:
                print(f"Printing number {i}")
                continue  # keep printing


n = int(input("Enter the limit: "))  # takes user input
num = Number(n)  # object creation
num.printNumbers()  # function call
