class Employee:  # class creation
    def __init__(self, ename):  # initialize constructor with 1 parameter
        self.ename = ename

    def printEmployee(self):  # method to print employee name
        return self.ename


class Manager:
    def __init__(self, mname):  # initialize constructor with 1 parameter
        self.mname = mname

    def printManager(self):  # method to print manager name
        return self.mname


class Hierarchy(Employee, Manager):  
    def __init__(self, ename, mname, cname):  # initialize constructor with 3 parameter
        Employee.__init__(self,ename)  # if we use super().__init__ here, then it will take only 1 parent class
        Manager.__init__(self,mname)  # so we explicitly use Class_name.__init__(self)
        self.cname = cname

    def printCompany(self):  # method to print company name
        return self.cname


ename = input("Enter the name of the employee: ")  # takes user input
mname = input("Enter the name of the manager: ")
cname = input("Enter the name of the company: ")
h = Hierarchy(ename, mname, cname)  # object creation
print(h.printEmployee())  # function call
print(h.printManager())
print(h.printCompany())
