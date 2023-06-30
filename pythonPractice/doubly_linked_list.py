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

    def prepend(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def delete_last(self):
        self.tail.prev.next = None
        self.tail = self.tail.prev
        self.size -= 1

    def delete(self, target_data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == target_data:
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
                return
            current_node = current_node.next

    def print_all(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def print_reverse(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev

    # Search to see if the list contains data
    def search(self, target_data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == target_data:
                return True
            current_node = current_node.next
        return False


dll = DoublyLinkedList()
for color in ("violet", "indigo", "blue", "green", "yellow", "orange", "red"):
    dll.append(color)
# print(dll.search("blue"))
# print(dll.search("gray"))
# dll.delete("blue")
# dll.print_reverse()
dll.delete_last()
dll.prepend("white")
dll.print_all()
