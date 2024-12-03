class count_Lines:  # class creation
    def __init__(self, file):
        self.file = file
        
    def countLines(self):  # function to count the number of lines
        try:
            f = open(self.file, 'r')  # open the file in read mode
            lines = f.readlines()  # reads all the lines
            count = len(lines)  # calculates the total number of lines in the file
            return count  # returns the total count of file
        except FileNotFoundError:  # if file not found
            print("File not found")


file = input("Enter the file name: ")  # takes user input
f = count_Lines(file)  # object creation
print(f.countLines())  # function call
