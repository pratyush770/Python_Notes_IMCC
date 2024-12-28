import Calculatorutility as cal  # CalculatorUtility module
num1 = int(input("Enter the first number: "))  # takes input from user
num2 = int(input("Enter the second number: "))
while True:
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Exit")
    ch = int(input("Enter your choice: "))  # asks for user's choice
    match ch:
        case 1:
            cal.addition(num1, num2)
        case 2:
            cal.subtraction(num1, num2)
        case 3:
            cal.multiplication(num1, num2)
        case 4:
            cal.division(num1, num2)
        case 5:
            break
        case _:
            print("Please enter a valid input")
