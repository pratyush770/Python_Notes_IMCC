class Student:
    student = {  # creates a user-defined dictionary with 4 key-value pairs
        "name": "Pratyush",
        "age": 20,
        "phone": 7666234983,
        "clg": "IMCC"
    }
    def printDetails(self):  # method to print details
        print(f"The name of the student is {self.student["name"]}")  # retrieves the name of the student using its key
        print(f"The college of the student is {self.student["clg"]}")  # retrieves the college of the student using its key


s = Student()  # object creation
s.printDetails()  # method call
