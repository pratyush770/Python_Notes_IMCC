# Every element in linked_list is known as 'Node'
# Each node of a linked_list can store an element called a 'Data'
# A link or pointer to the next link is called 'Next'
# A linked_list contains the link to the first node called 'Head'

class Linked_List:
    def __init__(self):
        self.head = None  # assign 'head' as null initially
    def append(self, node_value):
        self.head = node_value