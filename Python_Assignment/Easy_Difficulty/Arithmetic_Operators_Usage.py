class Arithmetic_Operators_Usage:
    def addition(self, n1, n2):  # function to add two numbers
        return n1 + n2  # adds two number using (+) operator

    def subtraction(self, n1, n2):  # function to subtract two numbers
        if n1 > n2:
            return n1 - n2  # subtracts two number using (-) operator
        else:
            return n2 - n1

    def multiplication(self, n1, n2):  # function to multiply two numbers
        return n1 * n2  # multiplies two number using (*) operator

    def division(self, n1, n2):  # function to divide two numbers
        if n1 > n2:
            return n1 / n2  # divides two number using (/) operator
        else:
            return n2 / n1

    def acceptInput(self, n1, n2):  # function to accept user input and display function accordingly
        while True:
            print("1) Addition")
            print("2) Subtraction")
            print("3) Multiplication")
            print("4) Division")
            print("5) Exit")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                print(self.addition(n1, n2))
            elif ch == 2:
                print(self.subtraction(n1, n2))
            elif ch == 3:
                print(self.multiplication(n1, n2))
            elif ch == 4:
                print(self.division(n1, n2))
            elif ch == 5:
                break
            else:
                print("Enter a valid choice")
