class declareAndAccessList:
    def __init__(self, n):
        self.n = n
    def declareAndAccessList(self):  # function to declare and access values in a list
        mylist = []  # empty list
        for i in range(self.n):
            val = int(input("Enter the value you want to add: "))
            mylist.append(val)  # appends each entered value in the list
        print()
        print(f"The elements of the list are as follows: {mylist}")  # prints the entire list
        print(f"The first element in the list is {mylist[0]}")  # prints the first element from the list
