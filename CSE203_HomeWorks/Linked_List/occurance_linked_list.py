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

    def num_of_occurrences(self, target_data):
        count = 0
        current_node = self.head
        while current_node is not None:
            if current_node.data == target_data:
                count += 1
            current_node = current_node.next
        return count


sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(2)
sll.append(2)
sll.append(4)
sll.append(2)
print(sll.num_of_occurrences(2))
