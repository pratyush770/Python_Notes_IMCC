class Calculator:
    def addition(self, num1, num2):   # method to add two numbers
        if num1 >= 0 and num2 >= 0:
            val = num1 + num2
            print(f"The addition of {num1} and {num2} is {val}")

    def subtraction(self, num1, num2):  # method to subtract two numbers
        if num1 >= 0 and num2 >= 0:
            val = num2 - num1
            print(f"The subtraction of {num2} and {num1} is {val}")

    def multiplication(self, num1, num2):  # method to multiply two numbers
        if num1 >= 0 and num2 >= 0:
            val = num1 * num2
            print(f"The multiplication of {num1} and {num2} is {val}")

    def division(self, num1, num2):  # method to divide two numbers
        if num2 != 0:
            val = num2 // num1
            print(f"The division of {num2} and {num1} is {val}")
        else:
            print("Cannot divide by zero")

    def acceptinput(self, inp, num1, num2):
        while True:
            if inp == 1:
                self.addition(num1, num2)
                break
            elif inp == 2:
                self.subtraction(num1, num2)
                break
            elif inp == 3:
                self.multiplication(num1, num2)
                break
            elif inp == 4:
                self.division(num1, num2)
                break
            else:
                print("Please enter a valid input")
                inp = int(input("Enter your choice again: "))  # if incorrect input is entered, then ask for input again

