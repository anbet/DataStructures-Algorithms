"""
    This is an implementation of AVL tree with its important properties implementation like
        height calculation, balance factor calculation, left rotation, right rotation and
        functions to check the avl properties
"""

class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
        self.height = 0


class Avl:
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
                # Calculate height of the node after each insertion
                node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1
        else:
            if node.right:
                self.insert_node(data, node.right)
            else:
                node.right = Node(data, node)
                node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1

        # After every insertion we need to check if the AVL tree's properties are violated
        self.handle_violation(node.parent)

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)
        else:
            return

    def remove_node(self, data, node):
        if node is None:
            return
        elif data < node.data:
            if node.left:
                self.remove_node(data, node.left)
        elif data > node.data:
            if node.right:
                self.remove_node(data, node.right)
        else:
            # There are three cases for the remove opration
            # case 1: if the node is leaf node
            if node.left is None and node.right is None:
                print(f"Removing leaf node {node.data}....")
                parent = node.parent
                if parent is not None and parent.left == node:
                    parent.left = None
                if parent is not None and parent.right == node:
                    parent.right = None

                # If Parent node is none then we need to remove root node
                if parent is None:
                    self.root = None

                del node
                self.handle_violation(parent)

            # Case 3: If node is having a single left child
            elif node.left is not None and node.right is None:
                print(f"Removing node with a single left node {node.data}....")
                parent = node.parent

                if parent.left == node and parent is not None:
                    parent.left = node.left
                if parent.right == node and parent is not None:
                    parent.right = node.left

                if parent is None:
                    self.root = node.left
                del node
                self.handle_violation(parent)
            # Case 4: If node is having a single right child
            elif node.right is not None and node.left is None:
                print(f"Removing node with a single right node {node.data}....")
                parent = node.parent

                if parent.left == node and parent is not None:
                    parent.left = node.right
                if parent.right == node and parent is not None:
                    parent.right = node.right

                if parent is None:
                    self.root = node.right
                del node
                self.handle_violation(parent)
            # Case 5: If node is having two children
            else:
                # Find the largest element in the left subtree
                print(f"Removing node with two child {node.data}...")
                predecessor = self.find_predecessor(self.root.left)
                # Swap the data of the node with two children with the predecessor idea is to do the mathematical reduction
                temp = node.data
                node.data = predecessor.data
                predecessor.data = temp
                # Now call the function recursively to delete the node
                self.remove_node(data, node)

    def find_predecessor(self, node):
        if node.right:
            return self.find_predecessor(node.right)
        return node

    # Calculate height of the node
    def calc_height(self, node):
        # If node is None then height of the node is -1
        if node is None:
            return -1
        # If node is not None then return the pre-computed height while inserting new node
        return node.height

    # The balance factor of parent determines if the tree is balanced or not
    # If the balance is greater than |1| then it is an imbalanced
    # Formula to determine the balance factor of tree is
    # |HEIGHT_left - HEIGHT_right|
    # If the balance is positive number > 1 then its left heavy
    # If the balance is negative number < -1 then its right heavy
    def calc_balance_factor(self, node):
        if node is None:
            return

        return self.calc_height(node.left) - self.calc_height(node.right)

    # we need to check for any violation of AVL property from the node we have inserted up to root node
    def handle_violation(self, node):

        while node is not None:
            # Re-Calculate the height of the node
            height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1
            # Make the needed rotation to balance any imbalances
            self.violation_helper(node)
            # Iterate up till root
            node = node.parent

    # This function is to check if there is an imbalance in the tree and make appropriate rotations
    def violation_helper(self, node):
        balance = self.calc_balance_factor(node)
        # If balance is greater than one then it is a left heavy situation
        if balance > 1:
            # Here can be two situation
            # 1: it can be left-right heavy situation
            if self.calc_balance_factor(node.left) < 0:
                self.rotate_left(node.left)

            # Then anyway make right rotation
            self.rotate_right(node)
        # If the balance is lesser than -1 then it is a right heavy situation
        if balance < -1:
            # 2: it can be right-left heavy situation
            if self.calc_balance_factor(node.right) > 0:
                self.rotate_right(node.right)

            # Then make a right rotation
            self.rotate_left(node)

    def rotate_left(self, node):
        if node is None:
            return
        print("Rotating left for node: %s and node.right: %s" % (node.data, node.right.data))
        temp_right_node = node.right
        t = temp_right_node.left

        # Now we need to attach the node to the left of temp_right_node for the rotation
        temp_right_node.left = node
        node.right = t

        if t is not None:
            t.parent = node

        # Now we need to assign the parents correctly since we have rotated the nodes
        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        # This is to re-assign the parent reference of old node
        if temp_right_node.parent is not None and temp_right_node.parent.left == node:
                temp_right_node.parent.left = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.right == node:
            temp_right_node.parent.right = temp_right_node

        # Now recalculate the height of the node and the temp node
        node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1
        temp_right_node.height = max(self.calc_height(temp_right_node.left), self.calc_height(temp_right_node.right)) + 1

    def rotate_right(self, node):
        if node is None:
            return
        print("Rotating right for node: %s and node.left: %s" % (node.data, node.left.data))
        temp_left_node = node.left
        t = temp_left_node.right

        # Now we need to attach the node to the left of temp_right_node for the rotation
        temp_left_node.right = node
        node.left = t

        # Re-assign parent of t
        if t is not None:
            t.parent = node

        # Now we need to assign the parents correctly since we have rotated the nodes
        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        # This is to re-assign the parent reference of old node
        if temp_left_node.parent is not None and temp_left_node.parent.left == node:
                temp_left_node.parent.left = temp_left_node
        if temp_left_node.parent is not None and temp_left_node.parent.right == node:
                temp_left_node.parent.right = temp_left_node

        node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1
        temp_left_node.height = max(self.calc_height(temp_left_node.left), self.calc_height(temp_left_node.right)) + 1

    def traverse(self):
        if self.root is not None:
            self.in_order_traverse(self.root)
        else:
            return
    def in_order_traverse(self, node):

        if node.left is not None:
            self.in_order_traverse(node.left)

        l = ''
        r = ''
        p = ''

        if node.left is not None:
            l = node.left.data
        else:
            l = 'None'
        if node.right is not None:
            r = node.right.data
        else:
            r = "None"

        if node.parent is not None:
            p = node.parent.data
        else:
            p = "None"

        print("current_node: %s left: %s right: %s parent: %s height: %s" % (node.data, l, r, p, node.height))

        if node.right is not None:
            self.in_order_traverse(node.right)


if __name__ == '__main__':
    avl = Avl()
    avl.insert(50)
    avl.insert(90)
    avl.insert(20)
    avl.insert(10)
    avl.insert(30)
    avl.insert(100)
    avl.insert(-9)
    avl.insert(2)
    avl.insert(150)
    avl.traverse()
