class Node:  # we do not import Node file since we require priority variable here
    def __init__(self, value, priority):
        self.data = value
        self.next = None
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):  # for inserting node in queue
        if self.front is None:
            self.front = self.rear = new_node
            return
        if self.rear:
            temp = self.front
            if self.front.priority > new_node.priority:  # for 1st position
                new_node.next = self.front
                self.front = new_node
                return
            while temp.next:
                if temp.next.priority >= new_node.priority:
                    break
                else:
                    temp = temp.next  # traverse
            new_node.next = temp.next
            temp.next = new_node  # updating rear pointer
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


q1 = PriorityQueue()
n1 = Node(10, 8)
n2 = Node(20, 4)
n3 = Node(30, 10)
n4 = Node(40, 7)
q1.enqueue(n1)
q1.enqueue(n2)
q1.enqueue(n3)
q1.enqueue(n4)
q1.print()
print()
q1.dequeue()  # will delete the queue with the lowest priority
q1.print()
