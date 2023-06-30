class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def average(self):
        li = list()
        current_node = self.head
        while current_node is not None:
            li.append(current_node.data)
            current_node = current_node.next
        avg = sum(li) / self.size
        return avg


dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(2)
# print(round(dll.average(), 2))
print('%0.2f' % dll.average())
