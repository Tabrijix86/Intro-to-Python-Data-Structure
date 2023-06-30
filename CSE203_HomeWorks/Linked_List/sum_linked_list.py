class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def node_sum(self):
        li = list()
        current_node = self.head
        while current_node is not None:
            li.append(current_node.data)
            current_node = current_node.next
        print(sum(li))


sll = SinglyLinkedList()
sll.append(10)
sll.append(10)
sll.append(10)
sll.append(10)
sll.append(10)
sll.node_sum()
