import Node as n


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # assign 'head' as null initially

    def create(self, node_value):  # method to append elements at end of doubly linked list
        temp = self.head  # points to 1st node
        if temp:
            while temp.next:  # find last node
                temp = temp.next
            temp.next = node_value  # appending new node
            node_value.prev = temp
        else:
            self.head = node_value  # add first node to the doubly linked list

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
                    temp.next = node_value
                    # we cannot write this line before the above 2 lines since we are updating the prev value of temp
                    return
                else:  # keep traversing
                    temp = temp.next
                    count += 1
                if temp is None:  # element not found in the doubly linked list
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
                if temp is None:  # element not found in the doubly linked list
                    print("Node is not present in the doubly linked list")
                    return
                temp.prev.next = temp.next  # create link between previous and next node
                if temp.next:  # will work only for position 2 till second last node and will skip the last node
                    temp.next.prev = temp

    def print(self):  # method to print elements of doubly linked list
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def reverse(self):
        temp = self.head
        prev = None
        # traverse all nodes of doubly linked list
        while temp:
            next_node = temp.next  # initially store the node value before reversing
            # reverse current node's next and prev pointer
            temp.next = prev
            temp.prev = next_node
            # move pointers one position ahead
            prev = temp
            temp = next_node
        self.head = prev  # update the head to the prev which is the last value after iteration


ll = DoublyLinkedList()
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
print()
ll.insert(n.Node(15), 2)
ll.print()
print()
print()
ll.delete(15)
ll.print()
print()
print()
ll.reverse()
ll.print()
