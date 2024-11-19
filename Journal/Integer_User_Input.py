from Integer_Methods import calculateFactorial, armstrongCheck
from Calculate_Area_Rect import calculateAreaRect

# 1) For calculating the factorial of a number
# n = int(input("Enter a number: "))   # takes input from the user
# calculateFactorial(n)  # function call

# 2) For checking if the number is armstrong or not
# n = int(input("Enter a number: "))   # takes input from the user
# armstrongCheck(n)  # function call

# 3) For calculating the area of a rectangle
length = int(input("Enter the length of the rectangle: "))   # takes input from the user
width = int(input("Enter the width of the rectangle: "))
rec = calculateAreaRect(length, width)
print(f"The area of the rectangle is {rec.getArea()}")
