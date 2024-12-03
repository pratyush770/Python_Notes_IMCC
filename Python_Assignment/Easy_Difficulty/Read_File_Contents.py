class read_File_Contents:
    def __init__(self, f):
        self.f = f

    def readFileContents(self):  # function to read file contents
        try:
            print("The contents of file are as follows...")
            for line in self.f:
                print(line.strip())  # removes whitespaces
        except FileNotFoundError:  # if file not found
            print("File not found")


fname = input("Enter the file name: ")  # takes user input
f = open(fname, "r")  # opens the file in read mode
print()
file = read_File_Contents(f)  # object creation
file.readFileContents()  # function call
