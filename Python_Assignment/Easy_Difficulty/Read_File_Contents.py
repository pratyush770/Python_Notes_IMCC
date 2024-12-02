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

