import Node as n


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None  # assign 'head' as null initially

    def create(self, node_value):  # method to append elements at end of doubly circular linked list
        temp = self.head  # points to 1st node
        if temp:
            while temp.next != self.head:  # find last node
                temp = temp.next
            temp.next = node_value  # appending new node
            node_value.prev = temp
            node_value.next = self.head
            self.head.prev = node_value
        else:
            self.head = node_value  # add first node to the doubly circular linked list
            node_value.next = self.head
            node_value.prev = self.head

    def insert(self, node_value, pos):  # method to insert element at specified position
        temp = self.head
        count = 1
        if pos == 1:
            while temp.next != self.head:
                temp = temp.next
            node_value.next = self.head
            self.head.prev = node_value
            node_value.prev = temp
            temp.next = node_value
            self.head = node_value  # making new_node as head
        else:
            while temp:
                if count+1 == pos:  # to stop the doubly circular linked list at 1 node before
                    node_value.next = temp.next
                    node_value.prev = temp
                    if temp.next:  # will work only for position 2 till second last node and will skip the last node
                        temp.next.prev = node_value
                    temp.next = node_value
                    # we cannot write this line before the above 2 lines since we are updating the prev value of temp
                    return
                else:  # keep traversing
                    temp = temp.next
                    count += 1
                if temp is None:  # element not found in the doubly circular linked list
                    print("Please enter a valid position")
                    return

    def delete(self, value):  # method to delete a specific element from the doubly circular linked list
        temp = self.head  # points to the 1st node
        temp1 = self.head  # extra pointer to traverse the list and find the last node
        if temp.data == value:  # node at 1st position
            while temp1.next != self.head:
                temp1 = temp1.next
            self.head = temp.next
            self.head.prev = temp1
            temp1.next = self.head
        else:  # for deleting the node other than 1st position
            while True:
                if temp.data == value:  # if node is found
                    break
                temp = temp.next  # go to the next element
                if temp == self.head:  # element not found in the doubly circular linked list
                    print("Node is not present in the doubly linked list")
                    return
            temp.prev.next = temp.next  # create link between previous and next node
            if temp.next:  # will work only for position 2 till second last node and will skip the last node
                temp.next.prev = temp.prev

    def print(self):  # method to print elements of doubly circular linked list
        temp = self.head
        while temp.next != self.head:
            print(temp.data, end=" ")
            temp = temp.next
        print(temp.data)


ll = DoublyCircularLinkedList()
n1 = n.Node(10)
n2 = n.Node(20)
n3 = n.Node(30)
n4 = n.Node(40)
ll.create(n1)
ll.create(n2)
ll.create(n3)
ll.create(n4)
ll.print()
print()
ll.insert(n.Node(15), 2)
ll.print()
print()
ll.delete(10)
ll.print()
