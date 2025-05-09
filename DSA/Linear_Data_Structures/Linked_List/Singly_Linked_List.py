import Node as n


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # assign 'head' as null initially

    def create(self, node_value):  # method to append elements at end of singly linked list
        temp = self.head  # points to 1st node
        if temp:
            while temp.next:  # find last node
                temp = temp.next
            temp.next = node_value  # appending new node
        else:
            self.head = node_value  # add first node to the singly linked list

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
                if temp is None:  # element not found in the singly linked list
                    print("Please enter a valid position")
                    return

    def delete(self, value):  # method to delete a specific element from the singly linked list
        temp = self.head  # points to the 1st node
        prev = None
        if temp.data == value:  # node at 1st position
            self.head = temp.next
        else:  # for deleting the node other than 1st position
            while temp:
                if temp.data == value:  # if node is found
                    break
                prev = temp
                temp = temp.next  # go to the next element
            if temp is None:  # element not found in the singly linked list
                print("Node is not present in the singly linked list")
                return
            if temp:
                prev.next = temp.next  # create link between previous and next node

    def print(self):  # method to print elements of singly linked list
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

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
        self.head = prev  # update the head to the prev which is the last value after iteration

    def count(self):  # method to get the count of nodes in the singly linked list
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        print(f"The number of nodes in the singly linked list is {count}")

    def min_max(self):  # method to get the min and max element in the singly linked list
        temp = self.head
        minimum, maximum = temp.data, temp.data  # min and max will point to the first node data
        while temp:
            if temp.data < minimum:
                minimum = temp.data
            if temp.data > maximum:
                maximum = temp.data
            temp = temp.next
        print(f"The minimum element in the singly linked list is {minimum}")
        print(f"The maximum element in the singly linked list is {maximum}")


ll = SinglyLinkedList()
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
ll.delete(40)
ll.print()
print()
print()
ll.reverse()
ll.print()
print()
print()
ll.count()
print()
ll.min_max()
