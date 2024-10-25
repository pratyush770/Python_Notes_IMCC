from Calculator import Calculator  # import the calculator method from calculator file
num1 = int(input("Enter the first number: "))  # takes input from user
num2 = int(input("Enter the second number: "))
c = Calculator()
print("1) Addition")
print("2) Subtraction")
print("3) Multiplication")
print("4) Division")
inp = int(input("Enter your choice (1,2,3,4): "))
c.acceptinput(inp, num1, num2)
