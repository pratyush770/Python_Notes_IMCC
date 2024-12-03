# Create a class Student with private attribute _name. Implement setter and getter methods for the attribute. 
# How would you set the name to "Alice" and then retrieve it?

class Student:
    def __init__(self):
        self._name = ""  # private attribute

    def setName(self, name):  # setter for setting the name of the student
        if len(name) == 0:  # edge case
            print("Please enter a name")
        else: 
            self._name = name
    
    def getName(self):  # getter to retrieve the name
        print(self._name)

    def printOtherDetails(self, age, phone):  # for printing the other details of student
        print(age)
        print(phone)
  

s = Student()  # object creation
s.setName(input("Enter the name of the student: "))  # for setting the name of the student
age = int(input("Enter the age of the student: "))
phone = int(input("Enter the phone number of the student: "))
s.getName()  # for retrieving the name of the student
s.printOtherDetails(age, phone)  # function call
