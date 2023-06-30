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

    def identical(self, list_2):
        a = self.head
        b = list_2.head
        while a is not None and b is not None:
            if a.data != b.data:
                return False
            else:
                a = a.next
                b = b.next
        return True


list_a = SinglyLinkedList()
list_b = SinglyLinkedList()

list_a.append(100)
list_a.append(20)
list_a.append(30)
list_a.append(40)
list_b.append(10)
list_b.append(20)
list_b.append(30)
list_b.append(40)

if list_a.identical(list_b) is True:
    print("Identical")
else:
    print("Non-identical")
