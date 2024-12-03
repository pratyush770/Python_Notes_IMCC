class Student:
    student = {  # creates a user-defined dictionary with 4 key-value pairs
        "name": "Pratyush",
        "age": 20,
        "phone": 7666234983,
        "clg": "IMCC"
    }

    def printDetails(self):  # method to print details
        return self.student["name"]  # retrieves the name of the student using its key


s = Student()  # object creation
print(s.printDetails())  # method call
