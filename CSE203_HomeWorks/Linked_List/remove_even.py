class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
        self.prev = None


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

    def remove_even(self):
        current_node = self.head
        while current_node is not None:
            if current_node.data % 2 == 0:
                if current_node == self.head:  # Deletion at the beginning of the list
                    self.head = current_node.next  # Update head
                    if current_node == self.tail:  # Only a single element
                        self.tail = None
                    else:
                        self.head.prev = None
                elif current_node == self.tail:  # Deletion at the end of the list
                    current_node.prev.next = None
                    self.tail = current_node.prev  # Update tail
                else:  # Deletion in the middle of the list
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                self.size -= 1
            current_node = current_node.next

    def print_all(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print("")


dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.append(6)
dll.append(7)
dll.remove_even()
dll.print_all()
