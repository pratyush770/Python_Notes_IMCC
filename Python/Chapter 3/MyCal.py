import Calculatorutility  # not using alias here
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
print()
res = Calculatorutility.addition(n1, n2)  # invoking addition method from CalculatorUtility class
print(f"The addition of {n1} and {n2} is {res}")
res = Calculatorutility.subtraction(n1, n2)
print(f"The subtraction of {n1} and {n2} is {res}")
res = Calculatorutility.division(n1, n2)
print(f"The division of {n1} and {n2} is {res}")
res = Calculatorutility.multiplication(n1, n2)
print(f"The multiplication of {n1} and {n2} is {res}")