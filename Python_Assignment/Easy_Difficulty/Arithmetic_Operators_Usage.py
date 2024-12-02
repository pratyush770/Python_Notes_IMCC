class Arithmetic_Operators_Usage:
    def addition(self, n1, n2):  # function to add two numbers
        print(f"The addition of {n1} and {n2} is {n1 + n2}")  # adds two number using (+) operator

    def subtraction(self, n1, n2):  # function to subtract two numbers
        if n1 > n2:
            print(f"The subtraction of {n1} and {n2} is {n1 - n2}")  # subtracts two number using (-) operator
        else:
            print(f"The subtraction of {n1} and {n2} is {n2 - n1}")

    def multiplication(self, n1, n2):  # function to multiply two numbers
        print(f"The multiplication of {n1} and {n2} is {n1 * n2}")  # multiplies two number using (*) operator

    def division(self, n1, n2):  # function to divide two numbers
        try:
            if n1 > n2:
                print(f"The division of {n1} and {n2} is {n1 / n2}")  # divides two number using (/) operator
            else:
                print(f"The division of {n1} and {n2} is {n2 / n1}")
        except ZeroDivisionError:
            print("Cannot divide by zero")

    def acceptInput(self, n1, n2):  # function to accept user input and display function accordingly
        while True:
            print("1) Addition")
            print("2) Subtraction")
            print("3) Multiplication")
            print("4) Division")
            print("5) Exit")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                self.addition(n1, n2)
            elif ch == 2:
                self.subtraction(n1, n2)
            elif ch == 3:
                self.multiplication(n1, n2)
            elif ch == 4:
                self.division(n1, n2)
            elif ch == 5:
                break
            else:
                print("Enter a valid choice")


