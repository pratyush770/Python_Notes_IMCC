import Node as n


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        value.next = self.top  # for previous values
        self.top = value

    def pop(self):
        temp = self.top
        if temp:
            print(f"Popped element: {temp.data}")
            self.top = temp.next  # will point to next element
            del temp  # will remove the top node
        else:
            print("Stack is empty")

    def print(self):
        temp = self.top
        print("The stack elements are...")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def reverse(self):
        st1 = Stack()  # create copy of stack
        temp = self.top
        while temp:
            new_node = n.Node(temp.data)  # create a new node with the same data
            st1.push(new_node)   # insert the new_node in the new stack
            temp = temp.next  # traverse the elements
        st1.print()   # print the new reversed stack

    def next_greatest_element(self):
        mylist = []
        temp = self.top
        while temp:
            mylist.append(temp.data)
            temp = temp.next  # traverse the elements
        mylist.sort(reverse=True)
        return mylist[1]

    def sort_stack(self):
        mylist = []
        temp = self.top
        while temp:
            mylist.append(temp.data)
            temp = temp.next  # Traverse the elements
        mylist.sort(reverse=True)
        sorted_stack = Stack()
        for item in mylist:
            sorted_stack.push(n.Node(item))  # Create a new node for each item
        return sorted_stack.print()

    def is_empty(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Stack is not empty")

    def reverse_string(self, str):
        st1 = Stack()
        for s in str:
            st1.push(n.Node(s))
        return st1.print()


st = Stack()
n1 = n.Node(10)
n2 = n.Node(20)
n3 = n.Node(30)
n4 = n.Node(40)
st.push(n1)
st.push(n2)
st.push(n3)
st.push(n4)
st.print()
print()
print(st.next_greatest_element())
st.sort_stack()
print()
st.pop()
st.print()
print()
st.reverse()
print()
st.is_empty()
st.reverse_string("Pratyush")


