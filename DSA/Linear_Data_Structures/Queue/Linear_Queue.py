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
        temp = self.front
        if self.rear:
            print(f"The deleted node is {temp.data}")
            self.front = self.front.next
            if self.front is None:  # for deleting last node in queue
                self.rear = None
            del temp
        else:
            print("Queue is empty")

    def count_occurences(self, node_val):
        temp = self.front
        count = 0
        while temp:
            if temp.data == node_val:
                count += 1
            temp = temp.next
        return count

    def search_queue(self, node_val):
        temp = self.front
        if temp.data == node_val:
            print("Node found")
            return
        else:
            while temp:
                if temp.data == node_val:
                    print("Node found")
                    return
                else:
                    temp = temp.next
        print("Node not found")

    def merge_queues(self, other_queue):
        temp = self.front
        while temp.next:
            temp = temp.next
        temp.next = other_queue.front

    def is_empty(self):
        return self.front is None

    def reverse(self):
        stack = []  # Stack to store nodes
        temp = self.front
        while temp:
            stack.append(temp)  # Push the node
            temp = temp.next
        if stack:
            self.front = stack.pop()  # Set the front to the first popped node
            temp = self.front
            while stack:
                temp.next = stack.pop()  # Reconnect nodes
                temp = temp.next
            temp.next = None  # Make sure the last node points to None

    def identical_queues(self, other_queue):
        temp = self.front
        temp1 = other_queue.front
        while temp and temp1:
            if temp.data != temp1.data:
                return False
            temp = temp.next
            temp1 = temp1.next
        return temp is None and temp1 is None


q1 = LinearQueue()
n1 = n.Node(10)
n2 = n.Node(20)
n3 = n.Node(30)
n4 = n.Node(30)
q1.enqueue(n1)
q1.enqueue(n2)
q1.enqueue(n3)
q1.enqueue(n4)
q1.print()
q2 = LinearQueue()
n1 = n.Node(10)
n2 = n.Node(20)
n3 = n.Node(30)
n4 = n.Node(30)
q2.enqueue(n1)
q2.enqueue(n2)
q2.enqueue(n3)
q2.enqueue(n4)
print(q1.identical_queues(q2))
print(q1.count_occurences(30))
q1.dequeue()
q1.print()
q1.search_queue(20)
q2 = LinearQueue()
node1 = n.Node(40)
node2 = n.Node(50)
q2.enqueue(node1)
q2.enqueue(node2)
q1.merge_queues(q2)
q1.print()
print(q1.is_empty())
q1.reverse()
q1.print()

