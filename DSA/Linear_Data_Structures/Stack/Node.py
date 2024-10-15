# Follows LIFO i.e. Last In First Out
# requires a top pointer which points to the top value
# used in: function calls, recursion, arithmetic expression evaluation, syntax parsing,
# memory management and backtracking
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
