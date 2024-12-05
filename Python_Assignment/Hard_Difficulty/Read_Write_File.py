class read_Write_File:  # class creation
    def __init__(self, file):
        self.file = file

    def readFile(self):  # function to read file
        try:
            f = open(self.file, "r")  # open the file in read mode
            lines = f.readlines()  # reads all the lines
            for l in lines: 
                print(l.strip())  # prints all the lines
        except FileNotFoundError:  # if file not found
            print("File not found")

    def writeFile(self):  # function to write file
        try:
            f = open(self.file, "w")  # open the file in write mode
            content = input("Enter the content you want to write: ")
            f.write(content)  # overwrites the existing content
        except FileNotFoundError:  # if file not found
            print("File not found")


file = input("Enter the file name: ")  # takes user input
f = read_Write_File(file)  # object creation
f.readFile()  # function call
f.writeFile()
    