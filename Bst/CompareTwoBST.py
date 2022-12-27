"""
Write an efficient algorithm thats able to compare two binary search trees. The method returns true if the trees are
identical (same topology with same values in the nodes) otherwise it returns false.
"""


class TreeComparator:

    def comparator(self, node1, node2):

        # This checks if the root node is null
        if not node1 or not node2:
            return node1 == node2

        # We need to check  the data of the nodes
        if node1.data is not node2.data:
            return False

        return self.comparator(node1.left, node2.left) and self.comparator(node1.right, node2.right)


class Node:
    def __init__(self, data, parent=None):
        self.root = None
        self.left = None
        self.right = None
        self.data = data
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):

        if data < node.data:
            if node.left:
                self.insert_node(data, node.left)
            else:
                node.left = Node(data, node)

        elif data > node.data:
            if node.right:
                self.insert_node(data, node.right)
            else:
                node.right = Node(data, node)

    def in_order_traverse(self):
        if self.root is None:
            return
        else:
            self.in_traverse(self.root)

    def in_traverse(self, node):
        if node.left:
            self.in_traverse(node.left)

        print(node.data)

        if node.right:
            self.in_traverse(node.right)


if __name__ == '__main__':
    bst1 = BinarySearchTree()

    bst1.insert(50)
    bst1.insert(90)
    bst1.insert(20)
    bst1.insert(10)
    bst1.insert(30)
    bst1.insert(100)
    bst1.insert(-9)
    bst1.insert(2)
    bst1.insert(150)

    bst2 = BinarySearchTree()
    bst2.insert(50)
    bst2.insert(90)
    bst2.insert(20)
    bst2.insert(10)
    bst2.insert(30)
    bst2.insert(100)
    bst2.insert(-9)
    bst2.insert(2)
    bst2.insert(150)

    bst1.in_order_traverse()
    compare = TreeComparator()
    print(compare.comparator(bst1.root, bst2.root))
