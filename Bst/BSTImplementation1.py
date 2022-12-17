"""
This Binary search tree implementation teaches following things:
    * How to hold the data of the BST
    * How abstract BST data type looks like
    * How to insert the data into BST
    * How to do an In-Order traversal of a BST
"""
class Node:
    def __init__(self, data, parent=None):
        self.right = None
        self.left = None
        self.data = data
        # This is important while we are implementing remove operation
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insertData(data, self.root)

    def insertData(self, data, node):
        if data < node.data:
            if node.left:
                self.insertData(data, node.left)
            else:
                node.left = Node(data, node)
        else:
            if node.right:
                self.insertData(data, node.right)
            else:
                node.right = Node(data, node)

    def inOrderTraversal(self):
        node = self.root
        self.traversal(node)

    def traversal(self, node):

        if node.left:
            self.traversal(node.left)

        print(node.data)

        if node.right:
            self.traversal(node.right)

if __name__ == '__main__':

    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(90)
    bst.insert(20)
    bst.insert(10)
    bst.insert(30)
    bst.insert(100)
    bst.insert(-9)
    bst.insert(2)
    bst.insert(150)

    bst.inOrderTraversal()


