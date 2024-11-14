# Rules for deleting a node in Binary Search Tree
# For leaf node: directly delete and make parent node as None
# For 1 child: Replace the value of parent node with the value of child node
# For 2 child: Replace with its inorder successor i.e. Left-Root-Right
# We need a left pointer, right pointer and data pointer for BST
class BinarySearchTree:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    def insert_node(self, new_node):
        if new_node.data < self.data:  # for inserting node at left
            if self.left is None:   # if there is no node at left
                self.left = new_node
                print(f"Node is inserted : {new_node.data}")
            else:  # if there is already a node at left
                self.left.insert_node(new_node)   # call the function again
        else:   # for inserting node at right
            if self.right is None:   # if there is no node at right
                self.right = new_node
                print(f"Node is inserted : {new_node.data}")
            else:  # if there is already a node at right
                self.right.insert_node(new_node)   # call the function again

    def inorder_traversal(self):  # Left-Root-Right
        if self.left:
            self.left.inorder_traversal()  # traverse left subtree
        print(self.data, end=' ')
        if self.right:
            self.right.inorder_traversal()  # traverse right subtree

    def preorder_traversal(self):  # Root-Left-Right
        print(self.data, end=' ')
        if self.left:
            self.left.preorder_traversal()  # traverse left subtree
        if self.right:
            self.right.preorder_traversal()  # traverse right subtree

    def postorder_traversal(self):  # Left-Right-Root
        if self.left:  # move to left side of tree
            self.left.postorder_traversal()  # traverse left subtree
        if self.right:  # move to right side of tree
            self.right.postorder_traversal()  # traverse right subtree
        print(self.data, end=' ')

    def search_node(self, val):
        if self.data == val:  # if node exists in the tree
            print(f"{val} exists")
            return
        elif val < self.data:  # for left child
            if self.left:  # move to left side of tree
                self.left.search_node(val)
            else:
                print(f"{val} does not exist")
                return
        else:   # for right child
            if self.right:  # move to right side of tree
                self.right.search_node(val)
            else:
                print(f"{val} does not exist")
                return

    def count_nodes(self):
        count = 1
        if self.left:
            count += self.left.count_nodes()  # increment count every time new function is called
        if self.right:
            count += self.right.count_nodes()
        return count

    def min_value(self):
        if self.left is None:  # we get minimum value
            print(f"Minimum value in the tree is {self.data}")
            return
        else:  # we keep traversing on left side
            self.left.min_value()

    def max_value(self):
        if self.right is None:  # we get minimum value
            print(f"Maximum value in the tree is {self.data}")
            return
        else:  # we keep traversing on right side
            self.right.max_value()

    # def min_max(self):   # alternative for min_max
    #     minimum = maximum = self.data
    #     if self.left:
    #         left_min, left_max = self.left.min_max()
    #         if left_min < minimum:  # calculate min of left subtree
    #             minimum = left_min
    #         if left_min > maximum:  # calculate max of left subtree
    #             maximum = left_min
    #     if self.right:
    #         right_min, right_max = self.left.min_max()
    #         if right_min < minimum:  # calculate min of right subtree
    #             minimum = right_min
    #         if right_min > maximum:  # calculate max of right subtree
    #             maximum = right_min
    #     return minimum, maximum

    def get_successor(self):
        curr = self.right  # will point to the right child node of current node
        while curr is not None and curr.left is not None:
            curr = curr.left   # will keep incrementing till we get the inorder successor
        return curr

    def delete_node(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_node(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_node(val)
        else:  # leaf node and node having one child
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            # when node has two children nodes
            successor = self.get_successor()
            self.data = successor.data
            self.right = self.right.delete_node(successor.data)  # deleting successor node
        return self


bst = BinarySearchTree(25)
bst.insert_node(BinarySearchTree(15))
bst.insert_node(BinarySearchTree(30))
bst.insert_node(BinarySearchTree(4))
bst.insert_node(BinarySearchTree(35))
bst.insert_node(BinarySearchTree(20))
bst.inorder_traversal()
print()
bst.preorder_traversal()
print()
bst.postorder_traversal()
print()
bst.search_node(20)
print()
print(bst.count_nodes())
print()
bst.min_value()
print()
bst.max_value()
# print()
# print(bst.min_max())
print()
print("Before deletion...")
bst.inorder_traversal()
print()
bst.delete_node(30)
print()
print("After deletion...")
bst.inorder_traversal()


