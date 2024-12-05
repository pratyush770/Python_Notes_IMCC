class operator_Overloading:  # class creation
    def __init__(self, num):  # initialize creation
        self.num = num

    def __add__(self, other):  # magic method to add two objects
        return self.num + other.num


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
obj1 = operator_Overloading(n1)  # first object creation
obj2 = operator_Overloading(n2)  # second object creation
print(obj1.__add__(obj2))  # adds two objects
