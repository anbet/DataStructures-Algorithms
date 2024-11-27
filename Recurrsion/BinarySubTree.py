class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_subtree(tree, subTree):
    if subTree is None:
        return True

    if tree is None:
        return False

    # Post Order Traversal
    po_tree = []
    po_subTree = []

    post_order(tree, po_tree)
    post_order(subTree, po_subTree)

    po_tree_1 = po_tree.__str__().replace("[", "").replace("]", "")
    po_tree_2 = po_subTree.__str__().replace("[", "").replace("]", "")

    if po_tree_1.find(po_tree_2) == -1:
        return False

    # In order traversal
    io_tree =[]
    io_subTree = []

    in_order(tree, io_tree)
    in_order(tree, io_subTree)

    io_tree_1 =  io_tree.__str__().replace("[", "").replace("]", "")
    io_tree_2 = io_subTree.__str__().replace("[", "").replace("]", "")

    if io_tree_1.find(io_tree_2) == -1:
        return False

    return True



def in_order(tree, li):
    if tree is None:
        return True

    in_order(tree.left, li)
    li.append(tree.data)
    in_order(tree.right, li)

def post_order(tree, li):
    if tree is None:
        return True

    li.append(tree.data)
    post_order(tree.left, li)
    post_order(tree.right, li)

root1 = Node(1);
root1.left = Node(2);
root1.right = Node(3);
root1.left.left = Node(4);
root1.left.right = Node(5);
root1.right.left = Node(6);
root1.right.right = Node(7);

root2 = Node(3)
root2.left = Node(6);
root2.right = Node(7);

is_a_subtree = is_subtree(root1, root2)
print(is_a_subtree)

# Time complexity is O(n + m)
# This is because we visit every node just once, so traversal of tree + subtree = (n + m)

# Space complexity is also O(n + m)