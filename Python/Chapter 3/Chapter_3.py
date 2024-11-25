# Functions in python
class Calculator:
    def __init__(self):
        pass

    def addition(self, num1, num2):  # function with parameters
        res = num1 + num2
        print(f"The addition of {num1} and {num2} is {res}")

    # * represents arbitrary argument
    def addition(self, *num):  # method overloading (takes n number of parameters)
        res = 0
        for n in num:
            res = res + n
        # print(f"Addition of all the numbers is {res}")
        # print(type(num))  # tuple is the datatype
        return res


def no_of_present_students(count=0):  # function taking default parameter
    print(f"The total number of students present in the lecture is {count}")


calObj = Calculator()
print(f"Addition of all the numbers is {calObj.addition(2, 3)}")
print(f"Addition of all the numbers is {calObj.addition(1, 2, 3, 4)}")
no_of_present_students(120)
no_of_present_students(175)
no_of_present_students()  # takes 0 since it is the default argument
