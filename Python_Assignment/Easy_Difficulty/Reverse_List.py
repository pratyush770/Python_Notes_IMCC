class reverse_List:
    def __init__(self, list):
        self.list = list

    def reverseList(self):  # function to reverse a list
        reversed_list = self.list[::-1]  # reverse the list using slicing
        return reversed_list  # return the reversed list


list = [1, 2, 3, 4, 5]  # list holding 5 elements
rl = reverse_List(list)
print(rl.reverseList())  # function call

