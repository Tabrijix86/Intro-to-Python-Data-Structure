class TreeNode:
    def __init__(self, new_data):
        self.data = new_data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)

    def add_left(self, node):
        self.left = node
        if node is not None:
            node.parent = self

    def add_right(self, node):
        self.right = node
        if node is not None:
            node.parent = self


def bst_insert(root, node):
    last_node = None
    current_node = root
    while current_node is not None:
        last_node = current_node
        if node.data < current_node.data:
            current_node = current_node.left
        else:
            current_node = current_node.right
    if last_node is None:
        root = node
    elif node.data < last_node.data:
        last_node.add_left(node)
    else:
        last_node.add_right(node)
    return root


def create_bst():
    root = TreeNode(10)
    for item in [5, 17, 3, 7, 12, 19, 1, 4]:
        node = TreeNode(item)
        root = bst_insert(root, node)
    return root


def search_bst(node, key):
    while node is not None:
        if node.data == key:
            return node
        if node.data > key:
            node = node.left
        else:
            node = node.right
    return node


def in_order(node):
    if node.left:
        in_order(node.left)
    print(node)
    if node.right:
        in_order(node.right)


def post_order(node):
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    print(node)


def pre_order(node):
    print(node)
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)


def bst_minimum(root):
    while root.left is not None:
        root = root.left
    return root


BST_root = create_bst()
print(BST_root)
# search_result = search_bst(BST_root, 7)
# print(search_result)
# in_order(BST_root)
# post_order(BST_root)
