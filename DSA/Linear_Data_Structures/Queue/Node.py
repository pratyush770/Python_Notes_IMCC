# Follows FIFO i.e. First In First Out
# requires a front and rear pointer which points to the first and last value respectively
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
