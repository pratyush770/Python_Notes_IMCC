class declareAndAccessList:
    def __init__(self, n):
        self.n = n

    def declareAndAccessList(self):  # function to declare and access values in a list
        mylist = [] # empty list
        for i in range(self.n):
            val = int(input("Enter the value you want to add: "))
            mylist.append(val)  # appends each entered value in the list
        print(mylist)  # prints the entire list
        return mylist[0]  # returns the first element from the list


n = int(input("Enter the number of elements you want to add in the list: "))  # takes user input
d = declareAndAccessList(n)  # object creation
print(d.declareAndAccessList())  # function call

