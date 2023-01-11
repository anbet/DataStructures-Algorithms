"""
This is implementation of BST using recursion
[ TO-DO ] : Correct the implementation of this logic from ALgoExpert.io
"""
import unittest


# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        node = self
        while node is not None:
            if value < node.value:
                if node.left:
                    node = node.left
                else:
                    node.left = BST(value)
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = BST(value)
                    break

        return self

    def contains(self, value):
        # Write your code here.
        global flag
        node = self
        flag = False
        while node is not None:
            # case 2: Navigate through left tree
            if value < node.value:
                if node.left:
                    node = node.left
            # case 3: Navigate through right tree
            elif value > node.value:
                    node = node.right
            # Check for node.value matches the value
            else:
                    flag = True
                    break
        return flag

    def remove(self, value, parent=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value < self.value:
            if self.left:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right:
                self.right.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.getMinValue()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.right = self.right.right
                    self.left = self.right.left
                else:
                    # do nothing for a single node tree
                    pass
            elif parent.left == self:
                if parent.left is not None:
                    parent.left = self.left
                else:
                    parent.left = self.right
            elif parent.right == self:
                if parent.right is not None:
                    parent.right = self.right
                else:
                    parent.right = self.left
        return self

    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()



    def traverse(self):
        node = self
        if node is not None:
            self.in_order_traverse(node)
        else:
            return

    def in_order_traverse(self, node):
        if node.left is not None:
            self.in_order_traverse(node.left)

        print(node.value)

        if node.right is not None:
            self.in_order_traverse(node.right)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)

        root.insert(12)
        self.assertTrue(root.right.left.left.value == 12)

        root.remove(10)
        root.traverse()
        self.assertTrue(not root.contains(10))
        self.assertTrue(root.value == 12)

        self.assertTrue(root.contains(15))