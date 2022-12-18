"""
This Binary search tree implementation is an extention of BSTImplementation1 and demonstrates below points:
    * use of return to evaluate the stack frame expression, you can refer to. Remove or add return statement to see the effects of the same
        * getMinValueFromBST function
        * inOrderTraversal function
    * This implementation includes two new methods
        * get max value
        * get min value
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

    def getMinValueFromBST(self):
        node = self.root
        if node.left:
            return self.getMinVal(node)

    def getMinVal(self, node):
        if node.left:
            # We need use return to remove reference of the stack frame, if we do not use return then we will always end
            # with root node as it always back tracks the expression to the root node

            # This behaviour can be seen in inorder Traversal method
            return self.getMinVal(node.left)

        return node.data

    def getMaxValueFromBST(self):
        node = self.root
        if node.right:
            return self.getMaxVal(node)

    def getMaxVal(self, node):

        if node.right:
           return self.getMaxVal(node.right)

        return node.data


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
    print("Min Val: %s" % bst.getMinValueFromBST())
    print("Max Val: %s" % bst.getMaxValueFromBST())
