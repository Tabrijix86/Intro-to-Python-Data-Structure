class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None


def add_node(tree, v):
    if tree is None:
        return Node(v)
    elif v >= tree.data:
        tree.right = add_node(tree.right, v)
    elif v < tree.data:
        tree.left = add_node(tree.left, v)
    return tree


def search_node(tree, search_data):
    if tree is None:
        return False
    elif tree.data == search_data:
        return True
    elif search_data > tree.data:
        return search_node(tree.right, search_data)
    elif search_data < tree.data:
        return search_node(tree.left, search_data)


def min_bst(tree):
    if tree is None:
        return None
    elif tree.left is None:
        return tree.data  # Here the root would be the minimum
    else:
        return min_bst(tree.left)
    # minBST(tree.left) means to send a new subtree minBST(tree)


def max_bst(tree):
    if tree is None:
        return None
    elif tree.right is None:
        return tree.data
    else:
        return max_bst(tree.right)  # minBST(tree.left) means sending a subtree minBST(tree)


def print_bst(tree):
    if tree is None:
        return
    print_bst(tree.left)
    print(tree.data, end=" ")
    print_bst(tree.right)


def remove(tree, to_be_removed):
    if tree is None:
        return None
    elif to_be_removed > tree.data:
        tree.right = remove(tree.right, to_be_removed)
    elif to_be_removed < tree.data:
        tree.left = remove(tree.left, to_be_removed)
    else:
        # a) if there is no child of root node
        if tree.left is None and tree.right is None:
            return None
        # b) if right child (right subtree) exist
        elif tree.left is None:
            return tree.right
        # c) if left child (left subtree) exist
        elif tree.right is None:
            return tree.left
        # d) if right child and left child( left subtree and right subtree) exist
        else:
            min_val = min_bst(tree.right)
            tree.data = min_val
            tree.right = remove(tree.right, min_val)
    return tree


def num_of_nodes(tree):
    if tree is None:
        return 0
    else:
        return 1 + num_of_nodes(tree.left) + num_of_nodes(tree.right)


def num_of_leaves(tree):
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        return 1
    else:
        return num_of_leaves(tree.left) + num_of_leaves(tree.right)


def main():
    tree = None
    tree = add_node(tree, 40)
    tree = add_node(tree, 30)
    tree = add_node(tree, 50)
    tree = add_node(tree, 20)
    tree = add_node(tree, 35)
    tree = add_node(tree, 43)
    tree = add_node(tree, 55)
    print_bst(tree)
    print("\nThe maximum is: ", max_bst(tree))
    print("The minimum is: ", min_bst(tree))
    print("Total number of nodes:", num_of_nodes(tree))
    print("Total number of leaves:", num_of_leaves(tree))


main()
