class calculateSquare:
    def __init__(self, mylist):
        self.mylist = mylist
    def calculateSquare(self):  # function to calculate square of numbers from 1 to 10
        squares = [i**2 for i in self.mylist]  # calculates square of each number using list comprehension
        print(squares)  # prints the list with its square


mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # list holding elements from 1 to 10
c = calculateSquare(mylist)  # object creation
c.calculateSquare()  # function call
