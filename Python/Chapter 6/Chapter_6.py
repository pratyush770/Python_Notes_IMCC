# Exception Handling
from UnderAgeUserError import UnderAgeUserError
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
try:
    res = (num1 // num2)
except ZeroDivisionError:
    print("Cannot divide by zero...")  # ZeroDivisionError
except:  # Bare excepts. Should be at end
    print("Another exception caught")
else:  # try-except-else is the format
    print(res)
finally:
    print("Thank you for using this code...")




