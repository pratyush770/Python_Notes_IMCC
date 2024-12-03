class student:
    student = [  # list of dictionaries
        {"name": "Ishana", "age": 16},
        {"name": "Pratyush", "age": 20},
        {"name": "Santosh", "age": 24}
    ]

    def sort_student_asc(self):  # function to sort the list of dictionary in ascending order by age
        student_asc = sorted(self.student, key=lambda x: x["age"])
        return student_asc

    def sort_student_desc(self):  # function to sort the list of dictionary in descending order by age
        student_desc = sorted(self.student, key=lambda x: x["age"], reverse=True)
        return student_desc
  
    def sort_student_above18(self):  # function to filter out the students having age < 18
        for s in self.student:
            if s["age"] < 18:
                self.student.remove(s)
        return self.student


s = student()  # object creation
print(s.sort_student_asc())  # function call
print(s.sort_student_desc())
print(s.sort_student_above18())
