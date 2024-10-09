# Every element in linked_list is known as 'Node'
# Each node of a linked_list can store an element called a 'Data'
# A link or pointer to the next link is called 'Next'
# A linked_list contains the link to the first node called 'Head'
from DSA.Linear_Data_Structures.Linked_List import Node as n
class Doubly_Linked_List:
    def __init__(self):
        self.head = None  # assign 'head' as null initially

    def append(self, node_value):  # method to append elements at end of doubly linked list
        temp = self.head  # points to 1st node
        if temp:
            while temp.next:  # find last node
                temp = temp.next
            temp.next = node_value  # appending new node
            node_value.prev = temp
        else:
            self.head = node_value  # add first node to the doubly linked list

    def print(self):  # method to print elements of doubly linked list
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def insert(self, node_value, pos):  # method to insert element at specified position
        temp = self.head
        count = 1
        if pos == 1:
            node_value.next = self.head
            self.head.prev = node_value
            self.head = node_value  # making new_node as head
        else:
            while temp:
                if count+1 == pos:  # to stop the doubly linked list at 1 node before
                    node_value.next = temp.next
                    node_value.prev = temp
                    if temp.next:  # will work only for position 2 till second last node and will skip the last node
                        temp.next.prev = node_value
                    temp.next = node_value  # we cannot write this line before the above 2 lines since we are updating the prev value of temp
                    return
                else:  # keep traversing
                    temp = temp.next
                    count += 1
                if temp == None:  # element not found in the doubly linked list
                    print("Please enter a valid position")
                    return

    def delete(self, value):  # method to delete a specific element from the doubly linked list
        temp = self.head  # points to the 1st node
        if temp.data == value:  # node at 1st position
            self.head = temp.next
            temp.next.prev = None  # we make prev as None, so it will not point to any node thus deleting the 1st node
        else:  # for deleting the node other than 1st position
            while temp:
                if temp.data == value:  # if node is found
                    break
                temp = temp.next  # go to the next element
                if temp == None:  # element not found in the doubly linked list
                    print("Node is not present in the doubly linked list")
                    return
                temp.prev.next = temp.next  # create link between previous and next node
                if temp.next:  # will work only for position 2 till second last node and will skip the last node
                    temp.next.prev = temp
        temp = None  # for deleting the node

    def count_min_max(self):  # method to get the count, min and max element in the doubly linked list
        temp = self.head
        count = 0
        min, max = temp.data, temp.data  # min and max will point to the first node data
        while temp:
            count += 1
            if temp.data < min:
                min = temp.data
            if temp.data > max:
                max = temp.data
            temp = temp.next
        print(f"The count of nodes in the singly linked list is {count}")
        print(f"The minimum element in the singly linked list is {min}")
        print(f"The maximum element in the singly linked list is {max}")

    def reverse(self):
        temp = self.head
        prev = None
        # traverse all nodes of doubly linked list
        while temp:
            next_node = temp.next
            # reverse current node's next pointer
            temp.next = prev
            # move pointers one position ahead
            prev = temp
            temp = next_node
        # return the head of the reversed doubly linked list
        return prev

ll = Doubly_Linked_List()
n1 = n.Node(10)
n2 = n.Node(20)
n3 = n.Node(30)
n4 = n.Node(40)
ll.append(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)
ll.print()
print()
ll.insert(n.Node(15), 8)
ll.print()
print()
ll.delete(15)
ll.print()
# print()
# ll.count_min_max()
# print()
# ll.head = ll.reverse()  # will return head value and while loop will execute every time, thus reversing the entire ll
# ll.print()
