# This file contains all the file methods

# 1) Without using readline() demonstrate a way in Python to read a multiline file line by line.
def readMultiLines(file):  # method to read a multiline file line by line without using readlines()
    try:
        f = open(file)  # opens the specified file in 'r' mode which is default mode
        f.seek(0)  # starts the file pointer from 0
        print(f"The contents of {file} are...")
        for i in f:
            print(i)  # prints the contents line by line
    except FileNotFoundError:
        print("File does not exist")


# 2) Using readlines() demonstrate a way to return the total number of NON BLANK lines in a file
def nonBlankLines(file):  # method to return the total number of non-blank lines in a file
    try:
        f = open(file)
        lines = f.readlines()  # reads all the lines from the specified file
        count = 0
        for i in lines:
            if i.strip():  # removes extra whitespaces thus returning only non-blank lines
                count += 1
        print(f"The number of non blank lines in {file} is {count}")
    except FileNotFoundError:
        print("File does not exist")


# 3) Using file writing methods, write a message from the user in a file. Show use of write when the file is in 'w' mode and 'a' mode
def writeReadDemo(file, msg, ap_msg):  # method to demonstrate the usage of 'w' and 'a' mode in file
    try:
        f = open(file, 'w')  # opens the specified file in 'w' mode
        f.write(msg)  # writes the user defined message in the file
        print("Content written successfully...")
        f = open(file)
        print(f.read())  # prints the contents of file after writing
        print()
        f = open(file, 'a')  # opens the specified file in 'a' mode
        f.write(ap_msg)
        print("Content appended successfully...")
        f = open(file)
        print(f.read())
    except FileNotFoundError:
        print("File does not exist")




