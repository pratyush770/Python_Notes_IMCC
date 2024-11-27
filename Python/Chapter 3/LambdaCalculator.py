# lambda functions
val1 = int(input("Enter the first number: "))
val2 = int(input("Enter the second number: "))
op = input("Enter choice ('add', 'sub', 'mul', 'div'): ")
op = op.lower()
addFunction = lambda val1, val2: val1 + val2  # lambda function and addFunction is the handler
if val1 > val2:
    subFunction = lambda val1, val2: val1 - val2
else:
    subFunction = lambda val1, val2: val2 - val1
mulFunction= lambda val1, val2: val1 * val2
if val1 > val2:
    divFunction = lambda val1, val2: val1 // val2
else:
    divFunction = lambda val1, val2: val2 // val1

while True:
    if op == 'add':
        print(f"The addition of {val1} and {val2} is {addFunction(val1, val2)}")
        break
    elif op == 'sub':
        print(f"The subtraction of {val1} and {val2} is {subFunction(val1, val2)}")
        break
    elif op == 'mul':
        print(f"The multiplication of {val1} and {val2} is {mulFunction(val1, val2)}")
        break
    elif op == 'div':
        print(f"The division of {val1} and {val2} is {divFunction(val1, val2)}")
        break
    else:
        print("Enter either add or sub")
        op = input("Enter add if you want to add the two numbers or sub if you want to subtract: ")
        op = op.lower()

# How to write a lambda function which has no parameters
# printHelloWorld = lambda: print("Hello World")
# printHelloWorld()

# Can we incorporate exception with lambda


