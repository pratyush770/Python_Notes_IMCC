# Without using readline() demonstrate a way in Python to read a multiline file line by line.

class readMultipleLines:
    def __init__(self, file):
        self.file = file

    def readMultiLines(self):  # method to read a multiline file line by line without using readlines()
        try:
            f = open(self.file)  # opens the specified file in 'r' mode which is default mode
            f.seek(0)  # starts the file pointer from 0
            print(f"The contents of {self.file} are...")
            for i in f:
                print(i)  # prints the contents line by line
        except FileNotFoundError:
            print("File does not exist")


fname = input("Enter the file name: ")
r = readMultipleLines(fname)
r.readMultiLines()
