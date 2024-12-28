from Student import Student

class Marksheet:
    def __init__(self):
        self.totalMks = 0  # public attribute
        self.percentage = 0

    def calculateMarks(self, mathsMks, scienceMks, engMks):   # method to calculate total marks
        self.totalMks = mathsMks + scienceMks + engMks
        print(f"The total marks are {self.totalMks}")

    def calculatePercentage(self):   # method to calculate total percentage
        self.percentage = (self.totalMks * 100) / 300
        print(f"The percentage of the student is {round(self.percentage, 2)}")


student = Student("", "", 0, 0, 0)
student.setName(input("Enter the student name: "))
student.setRollNumber(input("Enter the roll number of the student: "))
student.setMathsMks(int(input("Enter the maths marks: ")))
student.setScienceMks(int(input("Enter the science marks: ")))
student.setEngMks(int(input("Enter the english marks: ")))

marks = Marksheet()
marks.calculateMarks(student.getMathsMks(), student.getScienceMks(), student.getEngMks())
marks.calculatePercentage()
