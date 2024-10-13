# Every element in linked_list is known as 'Node'
# Each node of a linked_list can store an element called a 'Data'
# A link or pointer to the next link is called 'Next'
# A linked_list contains the link to the first node called 'Head'

class Node:
    def __init__(self, data):
        self.data = data  # for assigning the data
        self.next = None  # assign 'next' as null initially
        self.prev = None  # assign 'prev' as null initially
