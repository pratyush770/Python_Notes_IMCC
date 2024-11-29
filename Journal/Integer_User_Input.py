from Integer_Methods import calculateFactorial, armstrongCheck
# from Calculate_Area_Rect import calculateAreaRect
import Calculatorutility as cal

# 1) For calculating the factorial of a number
# n = int(input("Enter a number: "))   # takes input from the user
# calculateFactorial(n)  # function call

# 2) For checking if the number is armstrong or not
# n = int(input("Enter a number: "))   # takes input from the user
# armstrongCheck(n)  # function call

# 3) For calculating the area of a rectangle
# length = int(input("Enter the length of the rectangle: "))   # takes input from the user
# width = int(input("Enter the width of the rectangle: "))
# rec = calculateAreaRect(length, width)
# print(f"The area of the rectangle is {rec.getArea()}")

# 4) CalculatorUtility module
num1 = int(input("Enter the first number: "))  # takes input from user
num2 = int(input("Enter the second number: "))
while True:
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Exit")
    ch = int(input("Enter your choice: "))  # asks for user's choice
    if ch == 1:
        cal.addition(num1, num2)
    elif ch == 2:
        cal.subtraction(num1, num2)
    elif ch == 3:
        cal.multiplication(num1, num2)
    elif ch == 4:
        cal.division(num1, num2)
    elif ch == 5:
        break
    else:
        print("Please enter a valid input")


