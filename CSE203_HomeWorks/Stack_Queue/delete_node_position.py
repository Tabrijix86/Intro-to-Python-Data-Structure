class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_node(value, start):
    if value is None:
        return None

    if start < 1:
        return value

    if start == 1:
        return value.next

    value.next = delete_node(value.next, start - 1)
    return value


def push_ele(head_node, data):
    node = Node(0)
    node.data = data
    node.next = head_node
    head_node = node
    return head_node


def print_list(head_node):
    while head_node is not None:
        print(head_node.data, end="->")
        head_node = head_node.next

    print()


head = None

head = push_ele(head, 20)
head = push_ele(head, 4)
head = push_ele(head, 9)
head = push_ele(head, 18)
head = push_ele(head, 11)
head = push_ele(head, 33)
head = push_ele(head, 7)

print_list(head)

pos = 3
head = delete_node(head, pos)
print(f"After deleting node at {pos}th position")
print_list(head)
