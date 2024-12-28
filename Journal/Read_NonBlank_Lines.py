# Using readlines() demonstrate a way to return the total number of NON BLANK lines in a file

class readNonBlankLines:
    def __init__(self, file):
        self.file = file

    def nonBlankLines(self):  # method to return the total number of non-blank lines in a file
        try:
            f = open(self.file)
            lines = f.readlines()  # reads all the lines from the specified file
            count = 0
            for i in lines:
                if i.strip():  # removes extra whitespaces thus returning only non-blank lines
                    count += 1
            print(f"The number of non blank lines in {self.file} is {count}")
        except FileNotFoundError:
            print("File does not exist")


fname = input("Enter the file name: ")
n = readNonBlankLines(fname)
n.nonBlankLines()
