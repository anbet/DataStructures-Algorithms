"""
Write a function that takes in a Binary search Tree(BST) and a target integer data and returns the closest data
to that target data contained in the BST

You can assume that there will be only one closest data
"""


class TreeComparator:

    def findClosestNodeInBst(self, tree, target):
        # We need variables to compare the previous differences
        diff = 999999
        prev_diff = 999999
        ele = 0
        tree = tree.root
        if tree is not None:
            # case 1: return the element immediately if difference is o or 1
            if abs(tree.data - target) == 1 or tree.data - target == 0:
                ele = tree.data
            # case 2: Check the nearest neighbour by checking the absolute data if difference
            else:
                diff = abs(tree.data - target)
                ele = self.recurrsive_compare(tree, target, diff, prev_diff, ele)

            return ele

    def recurrsive_compare(self, tree, target, diff, prev_diff, ele):
        diff = abs(tree.data - target)
        if diff < prev_diff:
            prev_diff = diff
            ele = tree.data
        if target < tree.data:
            if tree.left:
                return self.recurrsive_compare(tree.left, target, diff, prev_diff, ele)
        else:
            if tree.right:
                return self.recurrsive_compare(tree.right, target, diff, prev_diff, ele)
        return ele


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
    bst2 = BinarySearchTree()
    bst2.insert(10)
    bst2.insert(15)
    bst2.insert(22)
    bst2.insert(13)
    bst2.insert(14)
    bst2.insert(5)
    bst2.insert(5)
    bst2.insert(2)
    bst2.insert(1)

    compare = TreeComparator()
    # Nearst to 12 is 13
    print(compare.findClosestNodeInBst(bst2, 12))
