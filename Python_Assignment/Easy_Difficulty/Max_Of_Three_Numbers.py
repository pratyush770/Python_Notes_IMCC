class find_Max_Number:
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def findMaxNumber(self):  # function to find the maximum of three numbers
        if self.n1 > self.n2 and self.n1 > self.n3:  # check if first number is greater than second and third number
            return self.n1
        elif self.n2 > self.n1 and self.n2 > self.n3:  # check if second number is greater than first and third num
            return self.n2
        else:  # check if third number is greater than first and second number
            return self.n3


n1 = int(input("Enter the first number: "))  # takes user input
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
num = find_Max_Number(n1, n2, n3)  # object creation
print(num.findMaxNumber())  # function call
