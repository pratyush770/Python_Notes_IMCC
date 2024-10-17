import Node as n


class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None  # assign 'head' as null initially

    def append(self, node_value):  # method to append elements at end of singly circular linked list
        temp = self.head  # points to 1st node
        if temp:
            while temp.next != self.head:  # find last node
                temp = temp.next
            temp.next = node_value  # appending new node
        else:
            self.head = node_value  # add first node to the singly circular linked list
        node_value.next = self.head  # will be required for all the nodes to form link

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
                if temp is None:  # element not found in the singly circular linked list
                    print("Please enter a valid position")
                    return

    def print(self):  # method to print elements of singly linked list
        temp = self.head
        while temp.next != self.head:
            print(temp.data, end=" ")
            temp = temp.next
        print(temp.data)  # for last node

    def delete(self, value):  # method to delete a specific element from the singly circular linked list
        temp = self.head  # points to the 1st node
        prev = None
        if temp.data == value:  # node at 1st position
            while temp.next != self.head:  # find last node
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
        else:  # for deleting the node other than 1st position
            while True:
                if temp.data == value:  # if node is found
                    break
                prev = temp
                temp = temp.next  # go to the next element
                if temp == self.head:  # element not found in the singly circular linked list
                    print("Node is not present in the singly linked list")
                    return
            if temp:
                prev.next = temp.next  # create link between previous and next node

    # def reverse(self):
    #     temp = self.head
    #     prev = None
    #     last_node = self.head  # Remember the head node, as it will become the last node after reversing
    #     # traverse all nodes of singly linked list
    #     while True:
    #         next_node = temp.next  # initially store the node value before reversing
    #         # reverse current node's next pointer
    #         temp.next = prev
    #         # move pointers one position ahead
    #         prev = temp
    #         temp = next_node
    #         if temp == self.head:
    #             break
    #     self.head = prev  # update the head to the prev which is the last value after iteration
    #     last_node.next = self.head  # Make the old head (which is now the last node) point to the new head


ll = SinglyCircularLinkedList()
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
# print()
# ll.reverse()
# ll.print()
