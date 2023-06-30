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

    def sort(self):
        if self.size == 0:
            print("List is empty!")
        else:
            current_node = self.head
            while current_node.next is not None:
                index = current_node.next
                while index is not None:
                    if current_node.data > index.data:
                        temp = current_node.data
                        current_node.data = index.data
                        index.data = temp
                    index = index.next
                current_node = current_node.next

    def print_all(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print("")


dll = DoublyLinkedList()
dll.append(7)
dll.append(1)
dll.append(4)
dll.append(5)
dll.append(2)
dll.print_all()
dll.sort()
dll.print_all()
