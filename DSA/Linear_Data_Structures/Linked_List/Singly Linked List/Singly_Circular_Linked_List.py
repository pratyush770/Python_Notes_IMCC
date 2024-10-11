# Every element in linked_list is known as 'Node'
# Each node of a linked_list can store an element called a 'Data'
# A link or pointer to the next link is called 'Next'
# A linked_list contains the link to the first node called 'Head'
from DSA.Linear_Data_Structures.Linked_List import Node as n
class Singly_Circular_Linked_List:
    def __init__(self):
        self.head = None  # assign 'head' as null initially

    def append(self, node_value):  # method to append elements at end of singly linked list
        temp = self.head  # points to 1st node
        if temp:
            while temp.next != self.head:  # find last node
                temp = temp.next
            temp.next = node_value  # appending new node
        else:
            self.head = node_value  # add first node to the singly linked list
        node_value.next = self.head  # will be required for all the nodes to form link

    def print(self):  # method to print elements of singly linked list
        temp = self.head
        while temp.next != self.head:
            print(temp.data)
            temp = temp.next
        print(temp.data)  # for last node

    def insert(self, node_value, pos):  # method to insert element at specified position
        temp = self.head
        count = 1
        if pos == 1:
            while temp.next != self.head:  # find last node
                temp = temp.next
            node_value.next = self.head  # making new node as head
            self.head = node_value
            temp.next = self.head  # updating last node's pointer
        else:
            while temp:
                if count+1 == pos:  # to stop the singly linked list at 1 node before
                    node_value.next = temp.next
                    temp.next = node_value
                    return
                else:  # keep traversing
                    temp = temp.next
                    count += 1
                if temp == None:  # element not found in the singly linked list
                    print("Please enter a valid position")
                    return

    def delete(self, value):  # method to delete a specific element from the singly linked list
        temp = self.head  # points to the 1st node
        if temp.data == value:  # node at 1st position
            self.head = temp.next
            while temp.next != self.head:  # find last node
                temp = temp.next
            temp.next = self.head
        else:  # for deleting the node other than 1st position
            while True:
                if temp.data == value:  # if node is found
                    break
                prev = temp
                temp = temp.next  # go to the next element
                if temp == self.head:  # element not found in the singly linked list
                    print("Node is not present in the singly linked list")
                    return
            if temp:
                prev.next = temp.next  # create link between previous and next node
        temp = None  # for deleting the node

    def reverse(self):
        temp = self.head
        prev = None
        # traverse all nodes of singly linked list
        while temp:
            next_node = temp.next  # initially store the node value before reversing
            # reverse current node's next pointer
            temp.next = prev
            # move pointers one position ahead
            prev = temp
            temp = next_node
        # return the head of the reversed linked list
        return prev

ll = Singly_Circular_Linked_List()
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
ll.insert(n.Node(15), 2)
ll.print()
print()
ll.delete(10)
ll.print()
print()
# ll.count_min_max()
# print()
# ll.head = ll.reverse()  # will return head value and while loop will execute every time, thus reversing the entire ll
# ll.print()
