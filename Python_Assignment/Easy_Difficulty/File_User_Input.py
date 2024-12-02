from Read_File_Contents import read_File_Contents
from Append_Text_In_File import append_Text_In_File

# fname = input("Enter the file name: ")  # takes user input
# f = open(fname, "r")  # opens the file in read mode
# print()
# file = read_File_Contents(f)  # object creation
# file.readFileContents()  # function call

file = input("Enter the file name: ")  # takes user input
f = append_Text_In_File(file)  # object creation
f.appendTextInFile()  # function call
