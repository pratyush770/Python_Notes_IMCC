class Node:  # we do not import Node file since we require priority variable here
    def __init__(self, value, priority):
        self.data = value
        self.next = None
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):  # for inserting node in queue
        temp = self.front
        if self.rear:
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
            if new_node.next is None:  # Update rear if new_node is now the last node
                self.rear = new_node
        else:  # for first node
            self.front = self.rear = new_node
            return

    def peek(self):
        if self.rear:
            return self.rear.data
        else:
            raise Exception("Queue is empty")

    def print(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def dequeue(self):  # for deleting node in queue with the lowest priority
        temp = self.front
        if self.rear:
            print(f"The deleted node is {temp.data}")
            self.front = self.front.next
            if self.front is None:  # for deleting last node in queue
                self.rear = None
            del temp
        else:
            print("Queue is empty")

    def dequeue_highest_priority(self):  # for deleting the node with the highest priority
        # If there's only one node, delete it
        if self.front == self.rear:
            print(f"The deleted node is {self.rear.data}")
            del self.front
            self.front = self.rear = None
            return

        # Traverse to the second-to-last node
        temp = self.front
        while temp.next != self.rear:
            temp = temp.next

        # Delete the last node (highest priority)
        print(f"The deleted node is {self.rear.data}")
        del self.rear
        self.rear = temp
        self.rear.next = None  # Update the last node's next to None


q1 = PriorityQueue()
n1 = Node(10, 8)
n2 = Node(20, 4)
n3 = Node(30, 7)
n4 = Node(40, 10)
q1.enqueue(n1)
q1.enqueue(n2)
q1.enqueue(n3)
q1.enqueue(n4)
q1.print()
print()
print(q1.peek())
q1.dequeue_highest_priority()  # will delete the queue with the lowest priority
q1.print()

