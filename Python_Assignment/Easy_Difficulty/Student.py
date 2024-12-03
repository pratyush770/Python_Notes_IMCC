class student:  # class creation
    def __init__(self, name, age, phone):  # initializes a constructor with 3 parameters
        self.name = name  # public attributes
        self.age = age
        self.phone = phone

    def printValues(self):  # method to print the values
        print(self.name)
        print(self.age)
        print(self.phone)


name = input("Enter the name of the student: ")  # takes user input
age = int(input("Enter the age of the student: "))
phone = int(input("Enter the phone number of the student: "))
stud = student(name, age, phone)  # object creation
stud.printValues()  # function call
