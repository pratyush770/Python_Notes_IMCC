class Employee:
    def __init__(self, name, dept, sal):
        self.name = name  # public attributes
        self.dept = dept
        self.sal = sal

    def calculate_salary(self):  # method to calculate salary
        total_sal = 30 * self.sal
        print(f"The total salary of the employee is {total_sal}")


class SalesEmployee(Employee):
    def __init__(self, name, dept, sal, no_of_leads):
        super().__init__(name, dept, sal)  # call attributes of parent class using super()
        self.no_of_leads = no_of_leads

    def calculate_salary(self):  # override calculate_salary method
        total_sal = 30 * self.sal * self.no_of_leads
        print(f"The total salary of the sales employee is {total_sal}")


class ManufacturingEmployee(Employee):
    def __init__(self, name, dept, sal, no_of_extra_hours):
        super().__init__(name, dept, sal)
        self.no_of_extra_hours = no_of_extra_hours

    def calculate_salary(self):
        total_sal = 30 * self.sal * self.no_of_extra_hours
        print(f"The total salary of the manufacturing employee is {total_sal}")
