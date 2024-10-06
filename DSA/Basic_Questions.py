# 1) Check if number is prime or not
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#         return True
# num = int(input("Enter a number : "))
# if(is_prime(num)):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")


# 2) Sum of digits
# def sum_of_digits(n):
#     sum = 0
#     rem = 0
#     while(n>0):
#         rem = n%10
#         sum = sum + rem
#         n = n//10
#     return sum
# n = int(input("Enter a number : "))
# print(f"The sum of digits is {sum_of_digits(n)}")


# 3) Check if the number is palindrome or not
# def palindrome(n):
#     sum = 0
#     rem = 0
#     temp = n
#     while(n>0):
#         rem = n%10
#         sum = (sum * 10) + rem
#         n = n//10
#     if sum == temp:
#         print(f"The number {temp} is a palindrome number")
#     else:
#         print(f"The number {temp} is not a palindrome number")
# n = int(input("Enter a number : "))
# palindrome(n)


# 4) Pyramid pattern
# def pyramid1(n):
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             print("*", end=" ")
#         print()
# def pyramid2(n):
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             print(chr(64 + j), end=" ")
#         print()
# def pyramid3(n):
#     for i in range(n, 0, -1):
#         for j in range(1, i+1):
#             print("*", end=" ")
#         print()
# def pyramid4(n):
#     for i in range(1, n+1):   # row will increment
#         for j in range(i, 0, -1):   # columns value will decrement
#             print(j, end=" ")
#         print()
# def pyramid5(n):
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             print("*", end=" ")
#         print()
#     for i in range(n-1, 0, -1):
#         for j in range(1, i+1):
#             print("*", end=" ")
#         print()
# def pyramid6(n):
#     space = 0
#     for i in range(n, 0, -2):
#         print(" " * space, end = '')   # for inserting spaces
#         for j in range(1, i+1):
#             print(j, end=" ")
#         print()
#         space += 1   # increase number of spaces by 1 for each row
# n = int(input("Enter a number : "))
# pyramid1(n)
# pyramid2(n)
# pyramid3(n)
# pyramid4(n)
# pyramid5(n)
# pyramid6(n)


# 5) Class and object practice
# class Student:
#     def __init__(self, rno, name):   # __init__ is a constructor in python
#         self.rno = rno  # self is similar to 'this' operator which references the current object
#         self.name = name
#     def print(self):  # user-defined method
#         print(f"The student roll number is {self.rno}")
#         print(f"The student name is {self.name}")
# s1 = Student(2401121,"Pratyush")
# s1.print()


