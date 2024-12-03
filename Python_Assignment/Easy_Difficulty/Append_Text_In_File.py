class append_Text_In_File:
    def __init__(self, file):
        self.file = file

    def appendTextInFile(self):  # function to append text into a file
        try:
            f = open(self.file, "r")  # open the file in read mode
            print("The content of file before appending is...")
            print(f.read())  # print the content of the file
            f = open(self.file, "a")  # open the file in append mode
            f.write(" This line gets appended")
            f = open(self.file, "r")  # open the file in read mode
            print("The content of file after appending is...")
            print(f.read())  # print the content of the file
        except FileNotFoundError:  # if file not found
            print("File not found")


file = input("Enter the file name: ")  # takes user input
f = append_Text_In_File(file)  # object creation
f.appendTextInFile()  # function call


