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
        self.size += 1

    def median(self):
        current_node = self.head
        if self.size % 2 != 0:
            for i in range(self.size // 2):
                current_node = current_node.next
            print(current_node.data)
        else:
            for i in range((self.size - 1) // 2):
                current_node = current_node.next
            print(int((current_node.data + current_node.next.data) / 2))


sll = SinglyLinkedList()
sll.append(1)
# sll.append(2)
sll.append(3)
# sll.append(4)
sll.append(5)
# sll.append(6)
sll.append(7)
# sll.append(8)
sll.append(9)
sll.median()
