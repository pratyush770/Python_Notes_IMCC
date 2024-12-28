# Using file writing methods, write a message from the user in a file. Show use of write when the file is in 'w' mode and 'a' mode

class writeMessageInFile:
    def __init__(self, file, msg, ap_msg):
        self.file = file
        self.msg = msg
        self.ap_msg = ap_msg

    def writeReadDemo(self):  # method to demonstrate the usage of 'w' and 'a' mode in file
        try:
            f = open(self.file, 'w')  # opens the specified file in 'w' mode
            f.write(self.msg)  # writes the user defined message in the file
            print("Content written successfully...")
            f = open(self.file)
            print(f.read())  # prints the contents of file after writing
            print()
            f = open(self.file, 'a')  # opens the specified file in 'a' mode
            f.write(self.ap_msg)
            print("Content appended successfully...")
            f = open(self.file)
            print(f.read())
        except FileNotFoundError:
            print("File does not exist")


fname = input("Enter the file name: ")
message = input("Enter the message to write in file: ")
append_msg = input("Enter the message to append after writing: ")
rw = writeMessageInFile(fname, message, append_msg)
rw.writeReadDemo()
