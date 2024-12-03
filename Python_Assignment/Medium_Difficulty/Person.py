class Person:
    def __init__(self, name, age):  # initializes constructor and takes 2 parameters
        self.name = name  # public attributes
        self.age = age
    
    def printDetails(self):  # method to print the details
        print(self.name)
        print(self.age)

    def checkAgeAbove18(self):  # method to check if age is above 18 or not
        if self.age > 18:
            print("You are an adult")
        else:
            print("You are not an adult")


name = input("Enter the name of the person: ")  # takes user input
age = int(input("Enter the age of the person: "))
p = Person(name, age)  # object creation
p.printDetails()  # function call
p.checkAgeAbove18()
