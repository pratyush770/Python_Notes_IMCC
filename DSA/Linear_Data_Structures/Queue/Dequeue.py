import Node as n


class DeQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node, ch):  # for inserting node in queue
        if self.front is None:  # if no node is present
            self.front = self.rear = new_node
            return
        if ch == 'f':  # if append at front
            new_node.next = self.front
            self.front = new_node
        else:  # if append at rear
            self.rear.next = new_node
            self.rear = new_node

    def print(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def dequeue(self, ch):
        if self.rear:
            temp = self.front
            if self.front == self.rear:  # if only 1 node is present
                print(f"The deleted node is {temp.data}")
                self.front = self.rear = None
                del temp
                return
            if ch == 'f':  # for deleting node from front
                print(f"The deleted node is {self.front.data}")
                self.front = self.front.next
            else:  # for deleting node from rear
                while temp.next != self.rear:  # find last node
                    temp = temp.next
                temp.next = self.rear.next
                self.rear = temp
            del temp
        else:
            print("Queue is empty")


q1 = DeQueue()
n1 = n.Node(10)
n2 = n.Node(20)
n3 = n.Node(30)
q1.enqueue(n1, 'f')
q1.enqueue(n2, 'r')
q1.enqueue(n3, 'f')
q1.print()
print()
q1.dequeue('r')
q1.print()
