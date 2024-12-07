# The sum of all the numbers of a row is twice the sum of all the numbers of the previous rows
def pascalTriangle(n):
    spaces = n  # for spaces
    for i in range(1, n+1):
        for s in range(1, spaces+1):
            print(' ', end=' ')  # for spacing
        c = 1  # constant value i.e. 1
        for j in range(1, i+1):
            print(c, end="  ")
            c = c*(i-j) // j  # logic
        spaces -= 1  # decrement the number of spaces after each iteration
        print()  # new line


n = int(input("Enter the limit: "))  # takes user input
pascalTriangle(n)  # function call
