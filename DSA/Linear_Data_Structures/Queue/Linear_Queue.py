import Node as n


class LinearQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):  # for inserting node in queue
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node  # updating rear pointer
        else:  # for first node
            self.front = self.rear = new_node
            return

    def print(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def dequeue(self):  # for deleting node in queue
        if self.rear is not None:
            temp = self.front
            print(f"The deleted node is {temp.data}")
            self.front = self.front.next
            if self.front is None:  # for deleting last node in queue
                self.rear = None
            del temp
        else:
            print("Queue is empty")


q1 = LinearQueue()
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

