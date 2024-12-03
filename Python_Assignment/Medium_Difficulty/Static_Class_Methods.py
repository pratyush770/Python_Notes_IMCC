class student:  # class creation
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def addition(self):  
        print("Inside local method")
        return self.n1 + self.n2

    @staticmethod  
    def additionFunc(n1, n2):  # method to add 2 numbers using static method
        print("Inside static method")
        return n1 + n2
    
    @classmethod
    def addFunc(cls, n1, n2):  # method to add 2 numbers using class method
        print("Inside class method")
        return n1 + n2


n1 = int(input("Enter the first number: "))  # takes user input
n2 = int(input("Enter the second number: "))
s = student(n1, n2)  # object creation
print(s.addition())  # function call
print(student.additionFunc(n1, n2))  # we can call static method directly without need of object creation
print(student.addFunc(n1, n2))  # we can call class method directly without need of object creation
