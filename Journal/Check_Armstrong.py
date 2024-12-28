# Without using any readymade methods, write a program in Python to check if the given number is an
# Armstrong number or not. Take the number from the user.

class checkArmstrong:
    def __init__(self, num):
        self.num = num

    def armstrongCheck(self):  # method to check if the number is armstrong or not
        temp = self.num  # temporary variable which holds same value as the entered input
        sum = 0
        while self.num > 0:
            rem = self.num % 10
            sum = sum + (rem * rem * rem)
            self.num = self.num // 10
        if sum == temp:
            print(f"{temp} is an Armstrong number")
        else:
            print(f"{temp} is not an Armstrong number")


n = int(input("Enter a number: "))   # takes input from the user
a = checkArmstrong(n)
a.armstrongCheck()  # function call
