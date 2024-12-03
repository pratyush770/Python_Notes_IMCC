class readPrintThirdLine:
    def __init__(self, file):
        self.file = file
    
    def readPrintThirdLine(self):  # method to read and print third line
        try:
            f = open(self.file, "r")  # opens the file in read mode
            lines = f.readlines()  # reads all the lines and returns it in the form of a list
            count = len(lines)  # calculates the total number of lines
            if count >= 3:  
                return lines[2].strip()  # returns the third line from the file
            else:
                print("There should be at least 3 lines in the file")
        except FileNotFoundError:  # if file not found
            print("File not found")


file = input("Enter the file name: ")  # takes user input
f = readPrintThirdLine(file)  # object creation
print(f.readPrintThirdLine())  # function call
