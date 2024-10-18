import Node as n


class CircularQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):  # for inserting node in queue
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node  # updating rear pointer
        else:  # for first node
            self.front = self.rear = new_node
        new_node.next = self.front  # for circular link
        return

    def print(self):
        if self.front is None:  # if queue is empty
            print("Queue is empty")
            return
        temp = self.front
        while temp.next != self.front:
            print(temp.data, end=" ")
            temp = temp.next
        print(temp.data)  # for printing last node

    def dequeue(self):  # for deleting node in queue
        if self.rear is None:
            print("Queue is empty")
            return
        temp = self.front
        print(f"The deleted node is {temp.data}")
        if self.front == self.rear:  # for deleting last node in queue
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front  # rear points to update front
        del temp


q1 = CircularQueue()
n1 = n.Node(10)
n2 = n.Node(20)
n3 = n.Node(30)
q1.enqueue(n1)
q1.enqueue(n2)
q1.enqueue(n3)
q1.print()
print()
q1.dequeue()
q1.print()
q1.dequeue()
q1.print()
q1.dequeue()
q1.print()


