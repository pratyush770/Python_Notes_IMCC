class student:  # class creation
    def __init__(self, name, age, phone):  # initializes a constructor with 3 parameters
        self.name = name  # public attributes
        self.age = age
        self.phone = phone

    def printValues(self):  # method to print the values
        print(f"The name of the student is {self.name}")
        print(f"The age of the student is {self.age}")
        print(f"The phone number of the student is {self.phone}")
