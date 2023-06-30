class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.prev = None
        self.now = None
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
        self.size += 1

    def delete_alt(self):
        if self.head is None:
            return
        else:
            self.prev = self.head
            self.now = self.head.next
            print(self.prev.data, end=" ")
        while self.prev is not None and self.now is not None:
            self.prev.next = self.now.next
            self.now = None
            self.prev = self.prev.next
            if self.prev is not None:
                self.now = self.prev.next
            print(self.prev.data, end=" ")


sll = SinglyLinkedList()
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
sll.append(60)
sll.append(70)
sll.append(80)
sll.delete_alt()
