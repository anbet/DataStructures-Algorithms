"""
    Remove node from BST
                                            50
                                        20      90
                                    10      30      100
                                -9             35   95    150
                            -11       2

    Case: When there are two leaf node of the parent and we need to remove one leaf node

        In our case this is 2 -> leaf node( node.left = None and node.right = None )
        parent = -9
        node.data = 2

        Case: Remove right leaf node of the parent
        if node.left = None and node.right = None
           if parent is not None and parent.right = Node
                parent.right = None
                node.parent = None

        Case: Remove left node leaf node of the parent
        if parent.right is None and parent.left == Node
            if parent is not None and parent.left = Node
                parent.left = None
                node.parent = None

        if parent is None:
            self.root = None

    Case: When there is a single child node of the node that we want to remove

        example: we need to remove 100 from parent 90
        parent = 90
        node.data = 100
        node. right = 150

        if parent is not None  and parent.right = Node
            if node.left = None and node.right is not None
                parent.right = Node.right
                Node.right.parent = parent
            if node.left is not none and node.right = None
                parent.right = node.left
                node.left.parent = parent

        example: we need to remove 100 from parent 90
        parent = 90
        node.data = 30
        node.left = 35

        if parent is not None and parent.left = Node
            if node.left = None and node.right is not None
                parent.left = Node.right
                Node.right.parent = parent
            if node.left is not none and node.right = None
                parent.left = node.left
                node.left.parent = parent

        if parent is None:
            self.root = node.left
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

    def removeNode(self, data):
        if self.root:
            self.removeNodeFromBST(data, self.root)
        else:
            return

    def removeNodeFromBST(self, data, node):
        # If tree is empty then return
        if node is None:
            return

        if node is not None:
            if data < node.data:
                self.removeNodeFromBST(data, node.left)
            elif data > node.data:
                self.removeNodeFromBST(data, node.right)
            else:
                # Case: Remove a single leaf node
                if node is not None:
                    parent = node.parent
                    if node.left is None and node.right is None:
                        print("Removing a leaf node ....%d" % node.data)
                        if parent is not None and parent.right == node:
                            parent.right = None
                            node.parent = None
                        if parent is not None and parent.left == node:
                            parent.left = None
                            node.parent = None

                        if parent is None:
                            self.root = None
                        del node

                    # Case: Remove a node with single right child
                    elif node.left is None and node.right is not None:
                        print("Removing node a single right child ....%d" % node.data)
                        if parent is not None and parent.right == node:
                            parent.right = node.right
                            node.right.parent = parent
                        elif parent is not None and parent.left == node:
                            parent.left = node.right
                            node.right.parent = parent
                        del node

                    # Case: Remove a node with single left child
                    elif node.left is not None and node.right is None:
                        print("Removing node a single left child ....%d" % node.data)
                        if parent is not None and parent.right == node:
                            parent.right = node.left
                            node.left.parent = parent
                        elif parent is not None and parent.left == node:
                            parent.left = node.left
                            node.left.parent = parent
                        del node

                    else:
                        print("Removing node with two children..... %d" % node.data)
                        # Case 1. Remove root node

                        predecessor = self.find_Predecessor(self.root.left)

                        temp = self.root.data
                        self.root.data = predecessor.data
                        predecessor.data = temp
                        self.removeNode(data)




    def find_Predecessor(self, node):
        if node.right:
            return self.find_Predecessor(node.right)
        return node


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

    bst.removeNode(150)
    bst.removeNode(10)
    bst.inOrderTraversal()
