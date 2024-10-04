# Every element in linked_list is known as 'Node'
# Each node of a linked_list can store an element called a 'Data'
# A link or pointer to the next link is called 'Next'
# A linked_list contains the link to the first node called 'Head'
import Node as n
class Singly_Linked_List:
    def __init__(self):
        self.head = None  # assign 'head' as null initially

    def append(self, node_value):  # method to append elements at end of singly linked list
        temp = self.head  # points to 1st node
        if temp:
            while temp.next:  # find last node
                temp = temp.next
            temp.next = node_value  # appending new node
        else:
            self.head = node_value  # add first node to the singly linked list

    def print(self):  # method to print elements of singly linked list
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def insert(self, node_value, pos):  # method to insert element at specified position
        temp = self.head
        count = 1
        if pos == 1:
            node_value.next = self.head  # making new node as head
            self.head = node_value
        else:
            while temp:
                if count+1 == pos:  # to stop the singly linked list at 1 node before
                    node_value.next = temp.next
                    temp.next = node_value
                    return
                else:  # keep traversing
                    temp = temp.next
                    count += 1

    def delete(self, value):  # method to delete a specific element from the singly linked list
        temp = self.head  # points to the 1st node
        if temp.data == value:  # node at 1st position
            self.head = temp.next
        else:  # for deleting the node other than 1st position
            while temp:
                if temp.data == value:  # if node is found
                    break
                prev = temp
                temp = temp.next  # go to the next element
                if temp == None:  # element not found in the singly linked list
                    print("Node is not present in the singly linked list")
                    return
                prev.next = temp.next  # create link between previous and next node
        temp = None  # for deleting the node

    def count_min_max(self):  # method to get the count, min and max element in the singly linked list
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



ll = Singly_Linked_List()
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
ll.insert(n.Node(15),2)
ll.print()
print()
ll.delete(15)
ll.print()
print()
ll.count_min_max()
