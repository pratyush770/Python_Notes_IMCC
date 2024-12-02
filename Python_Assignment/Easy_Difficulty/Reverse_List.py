class reverse_List:
    def __init__(self, list):
        self.list = list
    def reverseList(self):  # function to reverse a list
        print(f"The list before reversing is {self.list}")  # print the original list
        reversed_list = self.list[::-1]  # reverse the list using slicing
        print(f"The list after reversing is {reversed_list}")  # print the reversed list


list = [1, 2, 3, 4, 5]  # list holding 5 elements
rl = reverse_List(list)
rl.reverseList()  # function call

