class Person:  # class creation
    def printPerson(self): 
        print("Inside person class")

class Student(Person):  # single inheritance
    def printStudent(self):
        print("Inside student class")

class StudentGraduation(Student):  # multilevel inheritance
    def printStudentGraduation(self):
        print("Inside student graduation class")
    
s = StudentGraduation()  # object creation
s.printPerson()  # calling parent class function with the help of child class
s.printStudent()  # calling parent class function with the help of child class
s.printStudentGraduation()  # calling child class function
